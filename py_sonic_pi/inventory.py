from dataclasses import dataclass, field
from enum import Enum
from abc import ABC, abstractmethod


class Generator(ABC):
    pass


@dataclass
class SynthParameterDefinition:
    name: str
    default_value: float
    min_value: float | None = None
    max_value: float | None = None


class Synth(Generator):
    def __init__(self):
        self._parameter_values: dict[str, float] = {}

    @abstractmethod
    def get_ruby_synth_name(self) -> str:
        raise NotImplementedError("Subclasses must implement get_ruby_synth_name()")

    @classmethod
    @abstractmethod
    def get_parameters_definitions(cls) -> list[SynthParameterDefinition]:
        raise NotImplementedError(
            "Subclasses must implement get_parameters_definitions()"
        )

    def _get_parameter_definition_by_name(
        self, parameter_name: str
    ) -> SynthParameterDefinition | None:
        for param in self.get_parameters_definitions():
            if param.name == parameter_name:
                return param
        return None

    def set_parameter_value(self, parameter_name: str, value: float):
        parameter = self._get_parameter_definition_by_name(parameter_name)
        if parameter is None:
            raise ValueError(
                f"Unknown parameter name: {parameter_name} for synth {self.get_ruby_synth_name()}"
            )
        if value < parameter.min_value or value > parameter.max_value:
            raise ValueError(
                f"Value {value} for parameter {parameter_name} is out of range [{parameter.min_value}, {parameter.max_value}] for synth {self.get_ruby_synth_name()}"
            )
        self._parameter_values[parameter_name] = value

    def get_parameter_value_by_name(self, parameter_name: str) -> float:
        if parameter_name not in self._parameter_values:
            raise ValueError(
                f"Parameter {parameter_name} has not been set for synth {self.get_ruby_synth_name()}"
            )
        return self._parameter_values[parameter_name]

    def get_parameter_names(self) -> list[str]:
        return list(self._parameter_values.keys())


class StockSampleName(Enum):
    BD_HAUS = "bd_haus"
    RIDE_TRI = "ride_tri"
    ELEC_TICK = "elec_tick"
    ELEC_SNARE = "elec_snare"
    DRUM_HEAVY_KICK = "drum_heavy_kick"
    DRUM_TOM_MID_SOFT = "drum_tom_mid_soft"
    DRUM_TOM_MID_HARD = "drum_tom_mid_hard"
    DRUM_TOM_LO_SOFT = "drum_tom_lo_soft"
    DRUM_TOM_LO_HARD = "drum_tom_lo_hard"
    DRUM_TOM_HI_SOFT = "drum_tom_hi_soft"
    DRUM_TOM_HI_HARD = "drum_tom_hi_hard"
    DRUM_SPLASH_SOFT = "drum_splash_soft"
    DRUM_SPLASH_HARD = "drum_splash_hard"
    DRUM_SNARE_SOFT = "drum_snare_soft"
    DRUM_SNARE_HARD = "drum_snare_hard"
    DRUM_CYMBAL_SOFT = "drum_cymbal_soft"
    DRUM_CYMBAL_HARD = "drum_cymbal_hard"
    DRUM_CYMBAL_OPEN = "drum_cymbal_open"
    DRUM_CYMBAL_CLOSED = "drum_cymbal_closed"
    DRUM_CYMBAL_PEDAL = "drum_cymbal_pedal"
    DRUM_BASS_SOFT = "drum_bass_soft"
    DRUM_BASS_HARD = "drum_bass_hard"
    ELEC_TRIANGLE = "elec_triangle"
    ELEC_LO_SNARE = "elec_lo_snare"
    ELEC_HI_SNARE = "elec_hi_snare"
    ELEC_MID_SNARE = "elec_mid_snare"
    ELEC_CYMBAL = "elec_cymbal"
    ELEC_SOFT_KICK = "elec_soft_kick"
    ELEC_FILT_SNARE = "elec_filt_snare"
    ELEC_FUZZ_TOM = "elec_fuzz_tom"
    ELEC_CHIME = "elec_chime"
    ELEC_BONG = "elec_bong"
    ELEC_TWANG = "elec_twang"
    ELEC_WOOD = "elec_wood"
    ELEC_POP = "elec_pop"
    ELEC_BEEP = "elec_beep"
    ELEC_BLIP = "elec_blip"
    ELEC_BLIP2 = "elec_blip2"
    ELEC_PING = "elec_ping"
    ELEC_BELL = "elec_bell"
    ELEC_FLIP = "elec_flip"
    ELEC_HOLLOW_KICK = "elec_hollow_kick"
    ELEC_TWIP = "elec_twip"
    ELEC_PLIP = "elec_plip"
    ELEC_BLUP = "elec_blup"
    GUIT_HARMONICS = "guit_harmonics"
    GUIT_E_FIFTHS = "guit_e_fifths"
    GUIT_E_SLIDE = "guit_e_slide"
    GUIT_EM9 = "guit_em9"
    MISC_BURP = "misc_burp"
    PERC_BELL = "perc_bell"
    PERC_SNAP = "perc_snap"
    PERC_SNAP2 = "perc_snap2"
    AMBI_SOFT_BUZZ = "ambi_soft_buzz"
    AMBI_SWOOSH = "ambi_swoosh"
    AMBI_DRONE = "ambi_drone"
    AMBI_GLASS_HUM = "ambi_glass_hum"
    AMBI_GLASS_RUB = "ambi_glass_rub"
    AMBI_HAUNTED_HUM = "ambi_haunted_hum"
    AMBI_PIANO = "ambi_piano"
    AMBI_LUNAR_LAND = "ambi_lunar_land"
    AMBI_DARK_WOOSH = "ambi_dark_woosh"
    AMBI_CHOIR = "ambi_choir"
    BASS_HIT_C = "bass_hit_c"
    BASS_HARD_C = "bass_hard_c"
    BASS_THICK_C = "bass_thick_c"
    BASS_DROP_C = "bass_drop_c"
    BASS_WOODSY_C = "bass_woodsy_c"
    BASS_VOXY_C = "bass_voxy_c"
    BASS_VOXY_HIT_C = "bass_voxy_hit_c"
    BASS_DNB_F = "bass_dnb_f"
    SN_DUB = "sn_dub"
    SN_DOLF = "sn_dolf"
    SN_ZOME = "sn_zome"
    BD_ADA = "bd_ada"
    BD_PURE = "bd_pure"
    BD_808 = "bd_808"
    BD_ZUM = "bd_zum"
    BD_GAS = "bd_gas"
    BD_SONE = "bd_sone"
    BD_ZOME = "bd_zome"
    BD_BOOM = "bd_boom"
    BD_KLUB = "bd_klub"
    BD_FAT = "bd_fat"
    BD_TEK = "bd_tek"
    LOOP_INDUSTRIAL = "loop_industrial"
    LOOP_COMPUS = "loop_compus"
    LOOP_AMEN = "loop_amen"
    LOOP_AMEN_FULL = "loop_amen_full"
    LOOP_GARZUL = "loop_garzul"
    LOOP_MIKA = "loop_mika"
    LOOP_BREAKBEAT = "loop_breakbeat"


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
    def __init__(self):
        self.attributes: dict[str, float] = {}

    def set_attr(self, attr_name: str, value: float):
        self.attributes[attr_name] = value

    def get_attr(self, attr_name: str) -> float | None:
        return self.attributes.get(attr_name)


class Note(PatternElement):
    def __init__(self, note: int):
        super().__init__()
        self.note = note
        self.sample: Sample | None = None


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
