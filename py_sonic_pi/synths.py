from py_sonic_pi.inventory import Synth, SynthParameterDefinition

# Common Parameters
AMP = SynthParameterDefinition(name="amp", default_value=1.0, min_value=0.0)
PAN = SynthParameterDefinition(
    name="pan", default_value=0.0, min_value=-1.0, max_value=1.0
)
ATTACK = SynthParameterDefinition(name="attack", default_value=0.0, min_value=0.0)
DECAY = SynthParameterDefinition(name="decay", default_value=0.0, min_value=0.0)
SUSTAIN = SynthParameterDefinition(name="sustain", default_value=0.0, min_value=0.0)
RELEASE = SynthParameterDefinition(name="release", default_value=1.0, min_value=0.0)
ATTACK_LEVEL = SynthParameterDefinition(
    name="attack_level", default_value=1.0, min_value=0.0
)
DECAY_LEVEL = SynthParameterDefinition(
    name="decay_level", default_value=1.0, min_value=0.0
)
SUSTAIN_LEVEL = SynthParameterDefinition(
    name="sustain_level", default_value=1.0, min_value=0.0
)
ENV_CURVE = SynthParameterDefinition(
    name="env_curve", default_value=2.0, min_value=1.0, max_value=7.0
)


class DullBell(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            ENV_CURVE,
        ]

    def get_ruby_synth_name(self) -> str:
        return "dull_bell"


class PrettyBell(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            ENV_CURVE,
        ]

    def get_ruby_synth_name(self) -> str:
        return "pretty_bell"


class Beep(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            ENV_CURVE,
        ]

    def get_ruby_synth_name(self) -> str:
        return "beep"


class Sine(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            ENV_CURVE,
        ]

    def get_ruby_synth_name(self) -> str:
        return "sine"


class Saw(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            ENV_CURVE,
            SynthParameterDefinition(
                name="cutoff", default_value=100.0, min_value=0.0, max_value=130.0
            ),
        ]

    def get_ruby_synth_name(self) -> str:
        return "saw"


class Pulse(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            ENV_CURVE,
            SynthParameterDefinition(
                name="cutoff", default_value=100.0, min_value=0.0, max_value=130.0
            ),
            SynthParameterDefinition(
                name="pulse_width", default_value=0.5, min_value=0.0, max_value=1.0
            ),
        ]

    def get_ruby_synth_name(self) -> str:
        return "pulse"


class Subpulse(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            ENV_CURVE,
            SynthParameterDefinition(
                name="cutoff", default_value=100.0, min_value=0.0, max_value=130.0
            ),
            SynthParameterDefinition(
                name="pulse_width", default_value=0.5, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(name="sub_amp", default_value=1.0),
            SynthParameterDefinition(name="sub_detune", default_value=-12.0),
        ]

    def get_ruby_synth_name(self) -> str:
        return "subpulse"


class Square(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            ENV_CURVE,
            SynthParameterDefinition(
                name="cutoff", default_value=100.0, min_value=0.0, max_value=130.0
            ),
        ]

    def get_ruby_synth_name(self) -> str:
        return "square"


class Tri(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            ENV_CURVE,
            SynthParameterDefinition(
                name="cutoff", default_value=100.0, min_value=0.0, max_value=130.0
            ),
            SynthParameterDefinition(
                name="pulse_width", default_value=0.5, min_value=0.0, max_value=1.0
            ),
        ]

    def get_ruby_synth_name(self) -> str:
        return "tri"


class Dsaw(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            ENV_CURVE,
            SynthParameterDefinition(
                name="cutoff", default_value=100.0, min_value=0.0, max_value=130.0
            ),
            SynthParameterDefinition(name="detune", default_value=0.1),
        ]

    def get_ruby_synth_name(self) -> str:
        return "dsaw"


class Dpulse(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            ENV_CURVE,
            SynthParameterDefinition(
                name="cutoff", default_value=100.0, min_value=0.0, max_value=130.0
            ),
            SynthParameterDefinition(name="detune", default_value=0.1),
            SynthParameterDefinition(
                name="pulse_width", default_value=0.5, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(
                name="dpulse_width", default_value=0.5, min_value=0.0, max_value=1.0
            ),
        ]

    def get_ruby_synth_name(self) -> str:
        return "dpulse"


class Dtri(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            ENV_CURVE,
            SynthParameterDefinition(
                name="cutoff", default_value=100.0, min_value=0.0, max_value=130.0
            ),
            SynthParameterDefinition(name="detune", default_value=0.1),
        ]

    def get_ruby_synth_name(self) -> str:
        return "dtri"


class Fm(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            ENV_CURVE,
            SynthParameterDefinition(
                name="cutoff", default_value=100.0, min_value=0.0, max_value=130.0
            ),
            SynthParameterDefinition(name="divisor", default_value=2.0),
            SynthParameterDefinition(name="depth", default_value=1.0),
        ]

    def get_ruby_synth_name(self) -> str:
        return "fm"


class ModFm(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            ENV_CURVE,
            SynthParameterDefinition(
                name="cutoff", default_value=100.0, min_value=0.0, max_value=130.0
            ),
            SynthParameterDefinition(name="divisor", default_value=2.0),
            SynthParameterDefinition(name="depth", default_value=1.0),
            SynthParameterDefinition(
                name="mod_phase", default_value=0.25, min_value=0.0
            ),
            SynthParameterDefinition(name="mod_range", default_value=5.0),
            SynthParameterDefinition(
                name="mod_pulse_width", default_value=0.5, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(
                name="mod_phase_offset", default_value=0.0, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(
                name="mod_invert_wave", default_value=0.0, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(
                name="mod_wave", default_value=1.0, min_value=0.0, max_value=3.0
            ),
        ]

    def get_ruby_synth_name(self) -> str:
        return "mod_fm"


class ModSaw(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            ENV_CURVE,
            SynthParameterDefinition(
                name="cutoff", default_value=100.0, min_value=0.0, max_value=130.0
            ),
            SynthParameterDefinition(
                name="mod_phase", default_value=0.25, min_value=0.0
            ),
            SynthParameterDefinition(name="mod_range", default_value=5.0),
            SynthParameterDefinition(
                name="mod_pulse_width", default_value=0.5, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(
                name="mod_phase_offset", default_value=0.0, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(
                name="mod_invert_wave", default_value=0.0, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(
                name="mod_wave", default_value=1.0, min_value=0.0, max_value=3.0
            ),
        ]

    def get_ruby_synth_name(self) -> str:
        return "mod_saw"


class ModDsaw(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            ENV_CURVE,
            SynthParameterDefinition(
                name="cutoff", default_value=100.0, min_value=0.0, max_value=130.0
            ),
            SynthParameterDefinition(
                name="mod_phase", default_value=0.25, min_value=0.0
            ),
            SynthParameterDefinition(name="mod_range", default_value=5.0),
            SynthParameterDefinition(
                name="mod_pulse_width", default_value=0.5, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(
                name="mod_phase_offset", default_value=0.0, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(
                name="mod_invert_wave", default_value=0.0, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(
                name="mod_wave", default_value=1.0, min_value=0.0, max_value=3.0
            ),
            SynthParameterDefinition(name="detune", default_value=0.1),
        ]

    def get_ruby_synth_name(self) -> str:
        return "mod_dsaw"


class ModSine(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            ENV_CURVE,
            SynthParameterDefinition(
                name="cutoff", default_value=100.0, min_value=0.0, max_value=130.0
            ),
            SynthParameterDefinition(
                name="mod_phase", default_value=0.25, min_value=0.0
            ),
            SynthParameterDefinition(name="mod_range", default_value=5.0),
            SynthParameterDefinition(
                name="mod_pulse_width", default_value=0.5, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(
                name="mod_phase_offset", default_value=0.0, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(
                name="mod_invert_wave", default_value=0.0, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(
                name="mod_wave", default_value=1.0, min_value=0.0, max_value=3.0
            ),
        ]

    def get_ruby_synth_name(self) -> str:
        return "mod_sine"


class ModBeep(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            ENV_CURVE,
            SynthParameterDefinition(
                name="cutoff", default_value=100.0, min_value=0.0, max_value=130.0
            ),
            SynthParameterDefinition(
                name="mod_phase", default_value=0.25, min_value=0.0
            ),
            SynthParameterDefinition(name="mod_range", default_value=5.0),
            SynthParameterDefinition(
                name="mod_pulse_width", default_value=0.5, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(
                name="mod_phase_offset", default_value=0.0, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(
                name="mod_invert_wave", default_value=0.0, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(
                name="mod_wave", default_value=1.0, min_value=0.0, max_value=3.0
            ),
        ]

    def get_ruby_synth_name(self) -> str:
        return "mod_beep"


class ModTri(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            ENV_CURVE,
            SynthParameterDefinition(
                name="cutoff", default_value=100.0, min_value=0.0, max_value=130.0
            ),
            SynthParameterDefinition(
                name="mod_phase", default_value=0.25, min_value=0.0
            ),
            SynthParameterDefinition(name="mod_range", default_value=5.0),
            SynthParameterDefinition(
                name="mod_pulse_width", default_value=0.5, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(
                name="mod_phase_offset", default_value=0.0, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(
                name="mod_invert_wave", default_value=0.0, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(
                name="mod_wave", default_value=1.0, min_value=0.0, max_value=3.0
            ),
        ]

    def get_ruby_synth_name(self) -> str:
        return "mod_tri"


class ModPulse(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            ENV_CURVE,
            SynthParameterDefinition(
                name="cutoff", default_value=100.0, min_value=0.0, max_value=130.0
            ),
            SynthParameterDefinition(
                name="mod_phase", default_value=0.25, min_value=0.0
            ),
            SynthParameterDefinition(name="mod_range", default_value=5.0),
            SynthParameterDefinition(
                name="mod_pulse_width", default_value=0.5, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(
                name="mod_phase_offset", default_value=0.0, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(
                name="mod_invert_wave", default_value=0.0, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(
                name="mod_wave", default_value=1.0, min_value=0.0, max_value=3.0
            ),
            SynthParameterDefinition(
                name="pulse_width", default_value=0.5, min_value=0.0, max_value=1.0
            ),
        ]

    def get_ruby_synth_name(self) -> str:
        return "mod_pulse"


class Tb303(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            ENV_CURVE,
            SynthParameterDefinition(
                name="cutoff", default_value=120.0, max_value=130.0
            ),
            SynthParameterDefinition(
                name="cutoff_min", default_value=30.0, max_value=130.0
            ),
            SynthParameterDefinition(
                name="cutoff_attack", default_value=0.0, min_value=0.0
            ),
            SynthParameterDefinition(
                name="cutoff_decay", default_value=0.0, min_value=0.0
            ),
            SynthParameterDefinition(
                name="cutoff_sustain", default_value=0.0, min_value=0.0
            ),
            SynthParameterDefinition(
                name="cutoff_release", default_value=1.0, min_value=0.0
            ),
            SynthParameterDefinition(
                name="cutoff_attack_level",
                default_value=1.0,
                min_value=0.0,
                max_value=1.0,
            ),
            SynthParameterDefinition(
                name="cutoff_decay_level",
                default_value=1.0,
                min_value=0.0,
                max_value=1.0,
            ),
            SynthParameterDefinition(
                name="cutoff_sustain_level",
                default_value=1.0,
                min_value=0.0,
                max_value=1.0,
            ),
            SynthParameterDefinition(
                name="res", default_value=0.9, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(
                name="wave", default_value=0.0, min_value=0.0, max_value=2.0
            ),
            SynthParameterDefinition(
                name="pulse_width", default_value=0.5, min_value=0.0, max_value=1.0
            ),
        ]

    def get_ruby_synth_name(self) -> str:
        return "tb303"


class Supersaw(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            ENV_CURVE,
            SynthParameterDefinition(
                name="cutoff", default_value=130.0, min_value=0.0, max_value=130.0
            ),
            SynthParameterDefinition(
                name="res", default_value=0.7, min_value=0.0, max_value=1.0
            ),
        ]

    def get_ruby_synth_name(self) -> str:
        return "supersaw"


class Hoover(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            ENV_CURVE,
            SynthParameterDefinition(
                name="cutoff", default_value=130.0, min_value=0.0, max_value=130.0
            ),
            SynthParameterDefinition(
                name="res", default_value=0.1, min_value=0.0, max_value=1.0
            ),
        ]

    def get_ruby_synth_name(self) -> str:
        return "hoover"


class Prophet(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            ENV_CURVE,
            SynthParameterDefinition(
                name="cutoff", default_value=110.0, min_value=0.0, max_value=130.0
            ),
            SynthParameterDefinition(
                name="res", default_value=0.7, min_value=0.0, max_value=1.0
            ),
        ]

    def get_ruby_synth_name(self) -> str:
        return "prophet"


class Zawa(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            ENV_CURVE,
            SynthParameterDefinition(
                name="cutoff", default_value=100.0, min_value=0.0, max_value=130.0
            ),
            SynthParameterDefinition(
                name="res", default_value=0.9, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(name="phase", default_value=1.0, min_value=0.0),
            SynthParameterDefinition(
                name="phase_offset", default_value=0.0, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(
                name="wave", default_value=3.0, min_value=0.0, max_value=3.0
            ),
            SynthParameterDefinition(
                name="invert_wave", default_value=0.0, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(
                name="range", default_value=24.0, min_value=0.0, max_value=90.0
            ),
            SynthParameterDefinition(
                name="disable_wave", default_value=0.0, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(
                name="pulse_width", default_value=0.5, min_value=0.0, max_value=1.0
            ),
        ]

    def get_ruby_synth_name(self) -> str:
        return "zawa"


class DarkAmbience(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            ENV_CURVE,
            SynthParameterDefinition(
                name="cutoff", default_value=110.0, min_value=0.0, max_value=130.0
            ),
            SynthParameterDefinition(
                name="res", default_value=0.7, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(name="detune1", default_value=12.0),
            SynthParameterDefinition(name="detune2", default_value=24.0),
            SynthParameterDefinition(
                name="noise", default_value=0.0, min_value=0.0, max_value=4.0
            ),
            SynthParameterDefinition(
                name="ring", default_value=0.2, min_value=0.1, max_value=50.0
            ),
            SynthParameterDefinition(
                name="room", default_value=70.0, min_value=0.1, max_value=300.0
            ),
            SynthParameterDefinition(
                name="reverb_time", default_value=100.0, min_value=0.0
            ),
        ]

    def get_ruby_synth_name(self) -> str:
        return "dark_ambience"


class Growl(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            ENV_CURVE,
            SynthParameterDefinition(
                name="cutoff", default_value=130.0, min_value=0.0, max_value=130.0
            ),
            SynthParameterDefinition(
                name="res", default_value=0.7, min_value=0.0, max_value=1.0
            ),
        ]

    def get_ruby_synth_name(self) -> str:
        return "growl"


class Hollow(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            ENV_CURVE,
            SynthParameterDefinition(
                name="cutoff", default_value=90.0, min_value=0.0, max_value=130.0
            ),
            SynthParameterDefinition(
                name="res", default_value=0.99, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(
                name="noise", default_value=1.0, min_value=0.0, max_value=4.0
            ),
            SynthParameterDefinition(
                name="norm", default_value=0.0, min_value=0.0, max_value=1.0
            ),
        ]

    def get_ruby_synth_name(self) -> str:
        return "hollow"


class MonoPlayer(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            SynthParameterDefinition(name="pre_amp", default_value=1.0, min_value=0.0),
            PAN,
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            ENV_CURVE,
            SynthParameterDefinition(
                name="cutoff_attack", default_value=0.0, min_value=0.0
            ),
            SynthParameterDefinition(
                name="cutoff_decay", default_value=0.0, min_value=0.0
            ),
            SynthParameterDefinition(name="cutoff_sustain", default_value=-1.0),
            SynthParameterDefinition(
                name="cutoff_release", default_value=1.0, min_value=0.0
            ),
            SynthParameterDefinition(
                name="cutoff_attack_level",
                default_value=100.0,
                min_value=0.0,
                max_value=130.0,
            ),
            SynthParameterDefinition(
                name="cutoff_decay_level",
                default_value=100.0,
                min_value=0.0,
                max_value=130.0,
            ),
            SynthParameterDefinition(
                name="cutoff_sustain_level",
                default_value=100.0,
                min_value=0.0,
                max_value=130.0,
            ),
            SynthParameterDefinition(
                name="cutoff_env_curve", default_value=2.0, min_value=1.0, max_value=7.0
            ),
            SynthParameterDefinition(
                name="cutoff_min", default_value=30.0, max_value=130.0
            ),
            SynthParameterDefinition(name="rate", default_value=1.0),
            SynthParameterDefinition(
                name="start", default_value=0.0, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(
                name="finish", default_value=1.0, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(
                name="res", default_value=0.0, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(
                name="cutoff", default_value=0.0, min_value=0.0, max_value=130.0
            ),
            SynthParameterDefinition(
                name="norm", default_value=0.0, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(name="pitch", default_value=0.0),
            SynthParameterDefinition(
                name="window_size", default_value=0.2, min_value=0.00005
            ),
            SynthParameterDefinition(
                name="pitch_dis", default_value=0.0, min_value=0.0
            ),
            SynthParameterDefinition(name="time_dis", default_value=0.0, min_value=0.0),
            SynthParameterDefinition(
                name="compress", default_value=0.0, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(
                name="threshold", default_value=0.2, min_value=0.0
            ),
            SynthParameterDefinition(
                name="clamp_time", default_value=0.01, min_value=0.0
            ),
            SynthParameterDefinition(name="slope_above", default_value=0.5),
            SynthParameterDefinition(name="slope_below", default_value=1.0),
            SynthParameterDefinition(
                name="relax_time", default_value=0.01, min_value=0.0
            ),
        ]

    def get_ruby_synth_name(self) -> str:
        return "mono_player"


class StereoPlayer(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return MonoPlayer().get_parameters_definitions()

    def get_ruby_synth_name(self) -> str:
        return "stereo_player"


class Blade(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            ENV_CURVE,
            SynthParameterDefinition(
                name="cutoff", default_value=100.0, min_value=0.0, max_value=130.0
            ),
            SynthParameterDefinition(
                name="vibrato_rate", default_value=6.0, min_value=0.0, max_value=20.0
            ),
            SynthParameterDefinition(
                name="vibrato_depth", default_value=0.15, min_value=0.0, max_value=5.0
            ),
            SynthParameterDefinition(
                name="vibrato_delay", default_value=0.5, min_value=0.0
            ),
            SynthParameterDefinition(
                name="vibrato_onset", default_value=0.1, min_value=0.0
            ),
        ]

    def get_ruby_synth_name(self) -> str:
        return "blade"


class Piano(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            SynthParameterDefinition(
                name="vel", default_value=0.2, min_value=0.0, max_value=1.0
            ),
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            SynthParameterDefinition(
                name="hard", default_value=0.5, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(
                name="stereo_width", default_value=0.0, min_value=0.0, max_value=1.0
            ),
        ]

    def get_ruby_synth_name(self) -> str:
        return "piano"


class Pluck(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            ATTACK,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            SynthParameterDefinition(
                name="noise_amp", default_value=0.8, min_value=0.0, max_value=1.0
            ),
            SynthParameterDefinition(
                name="max_delay_time",
                default_value=0.125,
                min_value=0.125,
                max_value=1.0,
            ),
            SynthParameterDefinition(
                name="pluck_decay", default_value=30.0, min_value=1.0, max_value=100.0
            ),
            SynthParameterDefinition(
                name="coef", default_value=0.3, min_value=-1.0, max_value=1.0
            ),
        ]

    def get_ruby_synth_name(self) -> str:
        return "pluck"


class SoundIn(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [AMP, PAN, SynthParameterDefinition(name="input", default_value=0.0)]

    def get_ruby_synth_name(self) -> str:
        return "sound_in"


class Noise(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            ENV_CURVE,
            SynthParameterDefinition(
                name="cutoff", default_value=110.0, min_value=0.0, max_value=130.0
            ),
            SynthParameterDefinition(
                name="res", default_value=0.0, min_value=0.0, max_value=1.0
            ),
        ]

    def get_ruby_synth_name(self) -> str:
        return "noise"


class Pnoise(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            ENV_CURVE,
            SynthParameterDefinition(
                name="cutoff", default_value=110.0, min_value=0.0, max_value=130.0
            ),
            SynthParameterDefinition(
                name="res", default_value=0.0, min_value=0.0, max_value=1.0
            ),
        ]

    def get_ruby_synth_name(self) -> str:
        return "pnoise"


class Bnoise(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            ENV_CURVE,
            SynthParameterDefinition(
                name="cutoff", default_value=110.0, min_value=0.0, max_value=130.0
            ),
            SynthParameterDefinition(
                name="res", default_value=0.0, min_value=0.0, max_value=1.0
            ),
        ]

    def get_ruby_synth_name(self) -> str:
        return "bnoise"


class Gnoise(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            ENV_CURVE,
            SynthParameterDefinition(
                name="cutoff", default_value=110.0, min_value=0.0, max_value=130.0
            ),
            SynthParameterDefinition(
                name="res", default_value=0.0, min_value=0.0, max_value=1.0
            ),
        ]

    def get_ruby_synth_name(self) -> str:
        return "gnoise"


class Cnoise(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            ATTACK,
            DECAY,
            SUSTAIN,
            RELEASE,
            ATTACK_LEVEL,
            DECAY_LEVEL,
            SUSTAIN_LEVEL,
            ENV_CURVE,
            SynthParameterDefinition(
                name="cutoff", default_value=110.0, min_value=0.0, max_value=130.0
            ),
            SynthParameterDefinition(
                name="res", default_value=0.0, min_value=0.0, max_value=1.0
            ),
        ]

    def get_ruby_synth_name(self) -> str:
        return "cnoise"


class BasicMonoPlayer(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            SynthParameterDefinition(name="rate", default_value=1.0),
            SynthParameterDefinition(
                name="cutoff", default_value=0.0, min_value=0.0, max_value=130.0
            ),
            SynthParameterDefinition(
                name="res", default_value=0.0, min_value=0.0, max_value=1.0
            ),
        ]

    def get_ruby_synth_name(self) -> str:
        return "basic_mono_player"


class BasicStereoPlayer(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            PAN,
            SynthParameterDefinition(name="rate", default_value=1.0),
            SynthParameterDefinition(
                name="cutoff", default_value=0.0, min_value=0.0, max_value=130.0
            ),
            SynthParameterDefinition(
                name="res", default_value=0.0, min_value=0.0, max_value=1.0
            ),
        ]

    def get_ruby_synth_name(self) -> str:
        return "basic_stereo_player"


class BasicMixer(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [AMP]

    def get_ruby_synth_name(self) -> str:
        return "basic_mixer"


class MainMixer(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            SynthParameterDefinition(name="amp", default_value=1.0),
            SynthParameterDefinition(name="pre_amp", default_value=1.0),
            SynthParameterDefinition(name="hpf", default_value=0.0),
            SynthParameterDefinition(name="lpf", default_value=135.5),
            SynthParameterDefinition(name="hpf_bypass", default_value=0.0),
            SynthParameterDefinition(name="lpf_bypass", default_value=0.0),
            SynthParameterDefinition(name="force_mono", default_value=0.0),
            SynthParameterDefinition(name="invert_stereo", default_value=0.0),
            SynthParameterDefinition(name="limiter_bypass", default_value=0.0),
            SynthParameterDefinition(name="leak_dc_bypass", default_value=0.0),
        ]

    def get_ruby_synth_name(self) -> str:
        return "main_mixer"
