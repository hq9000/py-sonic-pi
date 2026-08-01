import json
import random
import string
from dataclasses import dataclass, field
from enum import Enum
from abc import ABC, abstractmethod

INTERNAL_MASTER_GAIN_STATE_VALUE_NAME = "internal_master_gain"
INTERNAL_MASTER_GAIN_EFFECT_ID = "internal_master_gain"
INTERNAL_MASTER_TRACK_ID = "internal_master"


class Generator(ABC):
    def __init__(self):
        self.project: "Project" = None  # type: ignore


@dataclass
class StateValue:
    name: str
    initial_value: float
    target_value: float
    transition_change_per_bar: int
    project: "Project" = field(default=None, repr=False, init=False)  # type: ignore

    def get_ruby_state_value_name(self, project: "Project") -> str:
        return f"state_value_{project.id}_{self.name}"

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "initial_value": self.initial_value,
            "target_value": self.target_value,
            "transition_change_per_bar": self.transition_change_per_bar,
        }
    @classmethod
    def from_dict(cls, data: dict) -> "StateValue":
        return cls(
            name=data["name"],
            initial_value=data["initial_value"],
            target_value=data["target_value"],
            transition_change_per_bar=data["transition_change_per_bar"],
        )


@dataclass
class SynthParameterDefinition:
    name: str
    default_value: float
    min_value: float | None = None
    max_value: float | None = None


class Synth(Generator):
    def __init__(self):
        super().__init__()
        self._parameter_values: dict[str, float | StateValue] = {}

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

    def set_parameter_value(self, parameter_name: str, value: float | StateValue):
        parameter_definition = self._get_parameter_definition_by_name(parameter_name)

        value_to_check = value.target_value if isinstance(value, StateValue) else value

        if parameter_definition is None:
            raise ValueError(
                f"Unknown parameter name: {parameter_name} for synth {self.get_ruby_synth_name()}"
            )

        if (
            parameter_definition.min_value is not None
            and value_to_check < parameter_definition.min_value
        ):
            raise ValueError(
                f"Value {value} for parameter {parameter_name} is below the minimum value {parameter_definition.min_value} for synth {self.get_ruby_synth_name()}"
            )
        if (
            parameter_definition.max_value is not None
            and value_to_check > parameter_definition.max_value
        ):
            raise ValueError(
                f"Value {value} for parameter {parameter_name} is above the maximum value {parameter_definition.max_value} for synth {self.get_ruby_synth_name()}"
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

    def to_dict(self) -> dict:
        parameter_values = {}
        for name, value in self._parameter_values.items():
            if isinstance(value, StateValue):
                parameter_values[name] = {"type": "state_value_ref", "name": value.name}
            else:
                parameter_values[name] = value
        return {
            "ruby_synth_name": self.get_ruby_synth_name(),
            "parameter_values": parameter_values,
        }


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

    def to_dict(self) -> dict:
        return {
            "stock_sample_name": self.name.value if self.name else None,
            "sample_path": self.sample_path,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Sample":
        stock_name = None
        if data.get("stock_sample_name"):
            stock_name = StockSampleName(data["stock_sample_name"])
        return cls(
            stock_sample_name=stock_name,
            sample_path=data.get("sample_path"),
        )


@dataclass
class Sampler(Generator):
    sample: Sample | None = None

    def to_dict(self) -> dict:
        return {
            "type": "sampler",
            "sample": self.sample.to_dict() if self.sample else None,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Sampler":
        sample = Sample.from_dict(data["sample"]) if data.get("sample") else None
        return cls(sample=sample)


@dataclass
class EffectInstance(ABC):
    id: str = ""
    controllable: bool = False
    project: "Project" = field(default=None, repr=False, init=False)  # type: ignore

    @abstractmethod
    def get_ruby_effect_name(self) -> str:
        raise NotImplementedError("Subclasses must implement get_ruby_effect_name()")

    @abstractmethod
    def get_fx_params_dict(self) -> dict[str, float]:
        raise NotImplementedError("Subclasses must implement get_fx_params_dict()")

    def get_param_names(self) -> list[str]:
        return list(self.get_fx_params_dict().keys())

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "controllable": self.controllable,
            "effect_ruby_name": self.get_ruby_effect_name(),
            "params": self.get_fx_params_dict(),
        }

    @classmethod
    def from_dict(cls, data: dict) -> "EffectInstance":
        from py_sonic_pi.effects import get_effect_class_by_ruby_name

        effect_ruby_name = data["effect_ruby_name"]
        effect_class = get_effect_class_by_ruby_name(effect_ruby_name)
        if effect_class is None:
            raise ValueError(f"Unknown effect name: {effect_ruby_name}")
        effect_instance = effect_class(id=data["id"], controllable=data["controllable"])
        for param_name, param_value in data["params"].items():
            # Convert integer values back to SlideShape enum for shape fields
            if param_name.endswith("_slide_shape") and isinstance(param_value, int):
                param_value = SlideShape(param_value)
            setattr(effect_instance, param_name, param_value)
        return effect_instance


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

    def to_dict(self) -> dict:
        return {
            "type": "note",
            "note": self.note,
            "sample": self.sample.to_dict() if self.sample else None,
            "attributes": dict(self.attributes),
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Note":
        note = cls(note=data["note"])
        note.sample = Sample.from_dict(data["sample"]) if data.get("sample") else None
        for attr_name, attr_value in data.get("attributes", {}).items():
            note.set_attr(attr_name, attr_value)
        return note


@dataclass
class Sync(PatternElement):
    n_bars: int

    def to_dict(self) -> dict:
        return {
            "type": "sync",
            "n_bars": self.n_bars,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Sync":
        return cls(n_bars=data["n_bars"])


class Sleep(PatternElement):
    def __init__(self, duration_beats: float):
        self.duration_beats = duration_beats

    def to_dict(self) -> dict:
        return {
            "type": "sleep",
            "duration_beats": self.duration_beats,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Sleep":
        return cls(duration_beats=data["duration_beats"])


@dataclass
class Pattern:
    elements: list[PatternElement] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "elements": [el.to_dict() for el in self.elements],
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Pattern":
        elements = []
        for el_data in data["elements"]:
            el_type = el_data["type"]
            if el_type == "note":
                elements.append(Note.from_dict(el_data))
            elif el_type == "sync":
                elements.append(Sync.from_dict(el_data))
            elif el_type == "sleep":
                elements.append(Sleep.from_dict(el_data))
        return cls(elements=elements)


class GeneratorTrackType(Enum):
    SYNTH = "synth"
    SAMPLE = "sample"


@dataclass(kw_only=True)
class Track(ABC):
    id: str
    custom_effects: list[EffectInstance] = field(default_factory=list)
    amp: float = 1.0
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
                amp=self.amp,
                amp_slide=self.slide,
                amp_slide_shape=SlideShape.LINEAR,
                pan=self.pan,
                pan_slide=self.slide,
                pan_slide_shape=SlideShape.LINEAR,
                controllable=True,
            )
        )
        return all

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "custom_effects": [fx.to_dict() for fx in self.custom_effects],
            "amp": self.amp,
            "pan": self.pan,
            "muted": self.muted,
            "solo": self.solo,
            "slide": self.slide,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Track":
        track_type = data.get("track_type")
        if track_type == "generator":
            from py_sonic_pi.synths import get_synth_class_by_ruby_name

            generator_data = data.get("generator", {})
            generator_type = generator_data.get("generator_type")

            if generator_type == "synth":
                ruby_synth_name = generator_data.get("ruby_synth_name", "")
                synth_class = get_synth_class_by_ruby_name(ruby_synth_name)
                generator = synth_class()
                for param_name, param_value in generator_data.get("parameter_values", {}).items():
                    if isinstance(param_value, dict) and param_value.get("type") == "state_value_ref":
                        generator.set_parameter_value(param_name, StateValue(
                            name=param_value["name"],
                            initial_value=0,
                            target_value=0,
                            transition_change_per_bar=0,
                        ))
                    else:
                        generator.set_parameter_value(param_name, param_value)
            elif generator_type == "sampler":
                generator = Sampler.from_dict(generator_data)
            else:
                raise ValueError(f"Unknown generator_type: {generator_type}")

            pattern = Pattern.from_dict(data.get("pattern", {"elements": []}))
            effects = [EffectInstance.from_dict(fx) for fx in data.get("custom_effects", [])]

            return GeneratorTrack(
                id=data["id"],
                generator=generator,
                pattern=pattern,
                effects=effects,
                amp=data.get("amp", 1.0),
                pan=data.get("pan", 0.0),
                mute=data.get("muted", False),
                solo=data.get("solo", False),
            )
        elif track_type == "group":
            children = [cls.from_dict(child) for child in data.get("children", [])]
            effects = [EffectInstance.from_dict(fx) for fx in data.get("custom_effects", [])]
            return GroupTrack(
                id=data["id"],
                children=children,
                effects=effects,
                amp=data.get("amp", 1.0),
                pan=data.get("pan", 0.0),
                muted=data.get("muted", False),
                solo=data.get("solo", False),
            )
        else:
            raise ValueError(f"Unknown track_type: {track_type}")


class GeneratorTrack(Track):
    def __init__(
        self,
        id: str,
        generator: Generator,
        pattern: Pattern,
        effects: list[EffectInstance] = [],
        amp: float = 1.0,
        pan: float = 0.0,
        mute: bool = False,
        solo: bool = False,
    ):
        super().__init__(
            id=id, custom_effects=effects, amp=amp, pan=pan, muted=mute, solo=solo
        )
        self.generator = generator
        self.pattern = pattern

    def get_type(self) -> GeneratorTrackType:
        return (
            GeneratorTrackType.SYNTH
            if isinstance(self.generator, Synth)
            else GeneratorTrackType.SAMPLE
        )

    def to_dict(self) -> dict:
        data = super().to_dict()
        generator_dict = (
            self.generator.to_dict() if hasattr(self.generator, "to_dict") else {}
        )
        if generator_dict:
            generator_dict["generator_type"] = "synth" if isinstance(self.generator, Synth) else "sampler"
        data["track_type"] = "generator"
        data["generator"] = generator_dict
        data["pattern"] = self.pattern.to_dict()
        return data


class GroupTrack(Track):
    def __init__(
        self,
        id: str,
        children: list[Track],
        effects: list[EffectInstance] = [],
        amp: float = 1.0,
        pan: float = 0.0,
        muted: bool = False,
        solo: bool = False,
    ):
        super().__init__(
            id=id, custom_effects=effects, amp=amp, pan=pan, muted=muted, solo=solo
        )
        self.children = children

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["track_type"] = "group"
        data["children"] = [child.to_dict() for child in self.children]
        return data


class SlideShape(Enum):
    STEP = 0
    LINEAR = 1
    SINE = 2
    WELCH = 3
    SQUARED = 6
    CUBED = 7


class Project:
    def __init__(
        self,
        top_level_tracks: list[Track],
        beat_length_seconds: float = 0.5,
        state_values: list[StateValue] = [],
        id: str | None = None,
    ):
        from py_sonic_pi.effects import Gain

        self.top_level_tracks = top_level_tracks
        self.beat_length_seconds = beat_length_seconds
        self.state_values = state_values

        master_gain_state_value = StateValue(
            initial_value=1.0,
            target_value=1.0,
            transition_change_per_bar=0,
            name=INTERNAL_MASTER_GAIN_STATE_VALUE_NAME,
        )
        self.state_values.append(master_gain_state_value)

        self.master_track = GroupTrack(
            id=INTERNAL_MASTER_TRACK_ID,
            children=self.top_level_tracks,
            effects=[
                Gain(
                    id=INTERNAL_MASTER_GAIN_EFFECT_ID,
                    controllable=True,
                    gain=master_gain_state_value,
                )
            ],
            amp=1.0,
            pan=0.0,
            muted=False,
            solo=False,
        )

        self.id = id if id is not None else "".join(random.choices(string.ascii_lowercase, k=5))

        self._set_project_references()

    def _set_project_references(self):
        """Set the project reference on all Generators, StateValues, and EffectInstances."""
        # Set project reference on all state values
        for state_value in self.state_values:
            state_value.project = self

        # Traverse all tracks and set project references
        def _traverse_track(track: Track):
            # Set project reference on all effects in this track
            for fx in track.custom_effects:
                fx.project = self

            if isinstance(track, GeneratorTrack):
                # Set project reference on the generator
                track.generator.project = self

                # Set project reference on StateValues used as synth parameters
                if isinstance(track.generator, Synth):
                    for param_value in track.generator._parameter_values.values():
                        if isinstance(param_value, StateValue):
                            param_value.project = self
            elif isinstance(track, GroupTrack):
                # Recursively traverse child tracks
                for child in track.children:
                    _traverse_track(child)

        _traverse_track(self.master_track)

    def serialize(self) -> str:
        data = {
            "project_id": self.id,
            "beat_length_seconds": self.beat_length_seconds,
            "state_values": [sv.to_dict() for sv in self.state_values],
            "top_level_tracks": [t.to_dict() for t in self.top_level_tracks],
        }
        return json.dumps(data, indent=2)

    def deserialize(self, serialized_project: str)-> "Project":
        data = json.loads(serialized_project)
        beat_length_seconds = data["beat_length_seconds"]

        # Separate internal vs user state values
        user_state_values = []
        internal_state_values = []
        for sv_data in data["state_values"]:
            if sv_data.get("name") == INTERNAL_MASTER_GAIN_STATE_VALUE_NAME:
                internal_state_values.append(sv_data)
            else:
                user_state_values.append(StateValue.from_dict(sv_data))

        top_level_tracks = [Track.from_dict(t) for t in data["top_level_tracks"]]
        project = Project(
            top_level_tracks=top_level_tracks,
            beat_length_seconds=beat_length_seconds,
            state_values=user_state_values,
        )

        # Preserve the original project id so state value references remain valid
        if "project_id" in data:
            project.id = data["project_id"]

        # Restore internal state values (e.g. if fade_out was called before serialization)
        for sv_data in internal_state_values:
            for sv in project.state_values:
                if sv.name == INTERNAL_MASTER_GAIN_STATE_VALUE_NAME:
                    sv.target_value = sv_data["target_value"]
                    sv.transition_change_per_bar = sv_data["transition_change_per_bar"]

        return project

    def create_copy(self) -> "Project":
        serialized = self.serialize()
        return self.deserialize(serialized)

    def get_flat_list_of_generator_tracks(self) -> list[GeneratorTrack]:
        generator_tracks = []

        def _traverse(track: Track):
            if isinstance(track, GeneratorTrack):
                generator_tracks.append(track)
            elif isinstance(track, GroupTrack):
                for child in track.children:
                    _traverse(child)

        _traverse(self.master_track)

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

        _traverse(self.master_track)

        return controllable_fxs

    def fade_out(self, fade_time_bars: float):
        for state_value in self.state_values:
            if state_value.name == INTERNAL_MASTER_GAIN_STATE_VALUE_NAME:
                state_value.target_value = 0.0
                state_value.transition_change_per_bar = 1 / fade_time_bars

    def get_master_gain_state_value(self) -> StateValue:
        for state_value in self.state_values:
            if state_value.name == INTERNAL_MASTER_GAIN_STATE_VALUE_NAME:
                return state_value
        raise ValueError("Global gain state value not found in project.")
