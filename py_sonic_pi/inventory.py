from dataclasses import dataclass, field
from enum import Enum
from abc import ABC, abstractmethod


class Generator(ABC):
    pass


class Synth(Generator):
    @abstractmethod
    def get_ruby_synth_name(self) -> str:
        raise NotImplementedError("Subclasses must implement get_ruby_synth_name()")


class StockSampleName(Enum):
    BD_HAUS = "bd_haus"
    RIDE_TRI = "ride_tri"
    ELEC_TICK = "elec_tick"


class Sample:
    def __init__(
        self,
        stock_sample_name: StockSampleName | None = None,
        sample_path: str | None = None,
    ):
        self.name = stock_sample_name
        self.sample_path = sample_path
        if self.name is None and self.sample_path is None:
            raise ValueError("Either stock_sample_name or sample_path must be provided")


@dataclass
class Sampler(Generator):
    sample: Sample | None = None


class Tb303(Synth):
    def get_ruby_synth_name(self) -> str:
        return "tb303"


@dataclass
class EffectInstance(ABC):
    id: str = ""
    controllable: bool = False

    @abstractmethod
    def get_ruby_effect_name(self) -> str:
        raise NotImplementedError("Subclasses must implement get_ruby_effect_name()")

    @abstractmethod
    def get_fx_params_dict(self) -> dict[str, float]:
        raise NotImplementedError("Subclasses must implement get_fx_params_dict()")

    def get_param_names(self) -> list[str]:
        return list(self.get_fx_params_dict().keys())


class PatternElement(ABC):
    pass


@dataclass
class Note(PatternElement):
    note: float = 0.0
    amp: float = 1.0
    pan: float = 0.0
    attack_beats: float = 0.0
    decay_beats: float = 0.0
    sustain_beats: float = 0.5
    sustain_amp: float = 1.0
    release_beats: float = 0.0
    sample: Sample | None = None
    rate: float = 1.0


@dataclass
class Sync(PatternElement):
    n_bars: int


class Sleep(PatternElement):
    def __init__(self, duration_beats: float):
        self.duration_beats = duration_beats


@dataclass
class Pattern:
    elements: list[PatternElement] = field(default_factory=list)


class GeneratorTrackType(Enum):
    SYNTH = "synth"
    SAMPLE = "sample"


@dataclass(kw_only=True)
class Track(ABC):
    id: str
    custom_effects: list[EffectInstance] = field(default_factory=list)
    gain: float = 1.0
    pan: float = 0.0
    muted: bool = False
    solo: bool = False
    slide: float = 0.0

    def get_effects(self):
        from py_sonic_pi.effects import Panner

        all = list(self.custom_effects)
        all.append(
            Panner(
                id=f"track_{self.id}_gain_and_pan",
                amp=self.gain,
                amp_slide=self.slide,
                amp_slide_shape=SlideShape.LINEAR,
                pan=self.pan,
                pan_slide=self.slide,
                pan_slide_shape=SlideShape.LINEAR,
                controllable=True,
            )
        )
        return all


class GeneratorTrack(Track):
    def __init__(
        self,
        id: str,
        generator: Generator,
        pattern: Pattern,
        effects: list[EffectInstance] = [],
        gain: float = 1.0,
        pan: float = 0.0,
        mute: bool = False,
        solo: bool = False,
    ):
        super().__init__(
            id=id, custom_effects=effects, gain=gain, pan=pan, muted=mute, solo=solo
        )
        self.generator = generator
        self.pattern = pattern

    def get_type(self) -> GeneratorTrackType:
        return (
            GeneratorTrackType.SYNTH
            if isinstance(self.generator, Synth)
            else GeneratorTrackType.SAMPLE
        )


class GroupTrack(Track):
    def __init__(
        self,
        id: str,
        children: list[Track],
        effects: list[EffectInstance] = [],
        gain: float = 1.0,
        pan: float = 0.0,
        muted: bool = False,
        solo: bool = False,
    ):
        super().__init__(
            id=id, custom_effects=effects, gain=gain, pan=pan, muted=muted, solo=solo
        )
        self.children = children


class Project:
    def __init__(self, top_level_tracks: list[Track], beat_length_seconds: float = 0.5):
        self.top_level_tracks = top_level_tracks
        self.beat_length_seconds = beat_length_seconds

    def get_flat_list_of_generator_tracks(self) -> list[GeneratorTrack]:
        generator_tracks = []

        def _traverse(track: Track):
            if isinstance(track, GeneratorTrack):
                generator_tracks.append(track)
            elif isinstance(track, GroupTrack):
                for child in track.children:
                    _traverse(child)

        for top_level_track in self.top_level_tracks:
            _traverse(top_level_track)

        return generator_tracks

    def get_all_controllable_fxs(self) -> list[EffectInstance]:
        controllable_fxs = []

        def _traverse(track: Track):
            for fx in track.get_effects():
                if fx.controllable:
                    controllable_fxs.append(fx)
            if isinstance(track, GroupTrack):
                for child in track.children:
                    _traverse(child)

        for top_level_track in self.top_level_tracks:
            _traverse(top_level_track)

        return controllable_fxs


class SlideShape(Enum):
    STEP = 0
    LINEAR = 1
    SINE = 2
    WELCH = 3
    SQUARED = 6
    CUBED = 7
