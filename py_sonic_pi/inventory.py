from dataclasses import dataclass, field
from enum import Enum
from abc import ABC, abstractmethod

class Generator:
    pass

class Synth(Generator):
    pass

class StockSampleName(Enum):
    BD_HAUS = "bd_haus"

class Sample:
    def __init__(self, stock_sample_name: StockSampleName|None = None, sample_path: str|None = None):
        self.name = stock_sample_name
        self.sample_path = sample_path
        if self.name is None and self.sample_path is None:
            raise ValueError("Either stock_sample_name or sample_path must be provided")

@dataclass
class Sampler(Generator):
    sample: Sample|None = None


@dataclass
class EffectInstance(ABC):
    id: str = ""

    @abstractmethod
    def get_ruby_effect_name(self) -> str:
        raise NotImplementedError("Subclasses must implement get_ruby_effect_name()")

    @abstractmethod
    def get_fx_params_dict(self) -> dict[str, float]:
        raise NotImplementedError("Subclasses must implement get_fx_params_dict()")


class HPFilter(EffectInstance):
    cutoff: float = 0.0
    cutoff_slide: float = 0.0

    def __init__(self, id: str, cutoff: float = 0.0, cutoff_slide: float = 0.0):
        super().__init__(id=id)
        self.cutoff = cutoff
        self.cutoff_slide = cutoff_slide

    def get_ruby_effect_name(self) -> str:
        return "rhpf"

    def get_fx_params_dict(self) -> dict[str, float]:
        return {
            "cutoff": self.cutoff,
            "cutoff_slide": self.cutoff_slide
        }

class PatternElement(ABC):
    pass

@dataclass
class Note(PatternElement):
    note: float = 0.0
    amp: float = 1.0
    pan: float = 0.0
    attack_seconds: float = 0.0
    decay_seconds: float = 0.0
    sustain_seconds: float = 0.5
    release_seconds: float = 0.0
    sample: Sample|None = None
    rate: float = 1.0

@dataclass
class Sync(PatternElement):
    n_bars: int

class Sleep(PatternElement):
    def __init__(self, duration_beats: float):
        self.duration_beats = duration_beats


class Pattern(ABC):
    pass

@dataclass
class SamplePattern(Pattern):
    elements: list[PatternElement] = field(default_factory=list)
    every_n_bars: int = 1

class GeneratorTrackType(Enum):
    SYNTH = "synth"
    SAMPLE = "sample"
@dataclass(kw_only=True)
class Track(ABC):
    id: str
    effects: list[EffectInstance] = field(default_factory=list)
    gain: float = 1.0
    pan: float = 0.0
    mute: bool = False
    solo: bool = False


class GeneratorTrack(Track):

    def __init__(self, id: str, generator: Generator, pattern: Pattern, effects: list[EffectInstance] = [], gain: float = 1.0, pan: float = 0.0, mute: bool = False, solo: bool = False):
        super().__init__(id=id, effects=effects, gain=gain, pan=pan, mute=mute, solo=solo)
        self.generator = generator
        self.pattern = pattern

    def get_type(self) -> GeneratorTrackType:
        return GeneratorTrackType.SYNTH if isinstance(self.generator, Synth) else GeneratorTrackType.SAMPLE



class GroupTrack(Track):
    def __init__(self, id: str, children: list[Track], effects: list[EffectInstance] = [], gain: float = 1.0, pan: float = 0.0, mute: bool = False, solo: bool = False):
        super().__init__(id=id, effects=effects, gain=gain, pan=pan, mute=mute, solo=solo)
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

