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

    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)

    def set_env_curve(self, value: float):
        self.set_parameter_value(ENV_CURVE.name, value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_env_curve(self, value: float):
        self.set_parameter_value(ENV_CURVE.name, value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_env_curve(self, value: float):
        self.set_parameter_value(ENV_CURVE.name, value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_env_curve(self, value: float):
        self.set_parameter_value(ENV_CURVE.name, value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_cutoff(self, value: float):
        self.set_parameter_value("cutoff", value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_env_curve(self, value: float):
        self.set_parameter_value(ENV_CURVE.name, value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_cutoff(self, value: float):
        self.set_parameter_value("cutoff", value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_env_curve(self, value: float):
        self.set_parameter_value(ENV_CURVE.name, value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_pulse_width(self, value: float):
        self.set_parameter_value("pulse_width", value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_cutoff(self, value: float):
        self.set_parameter_value("cutoff", value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_env_curve(self, value: float):
        self.set_parameter_value(ENV_CURVE.name, value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_pulse_width(self, value: float):
        self.set_parameter_value("pulse_width", value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_sub_amp(self, value: float):
        self.set_parameter_value("sub_amp", value)

    def set_sub_detune(self, value: float):
        self.set_parameter_value("sub_detune", value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_cutoff(self, value: float):
        self.set_parameter_value("cutoff", value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_env_curve(self, value: float):
        self.set_parameter_value(ENV_CURVE.name, value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_cutoff(self, value: float):
        self.set_parameter_value("cutoff", value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_env_curve(self, value: float):
        self.set_parameter_value(ENV_CURVE.name, value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_pulse_width(self, value: float):
        self.set_parameter_value("pulse_width", value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_cutoff(self, value: float):
        self.set_parameter_value("cutoff", value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_detune(self, value: float):
        self.set_parameter_value("detune", value)

    def set_env_curve(self, value: float):
        self.set_parameter_value(ENV_CURVE.name, value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_cutoff(self, value: float):
        self.set_parameter_value("cutoff", value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_detune(self, value: float):
        self.set_parameter_value("detune", value)

    def set_dpulse_width(self, value: float):
        self.set_parameter_value("dpulse_width", value)

    def set_env_curve(self, value: float):
        self.set_parameter_value(ENV_CURVE.name, value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_pulse_width(self, value: float):
        self.set_parameter_value("pulse_width", value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_cutoff(self, value: float):
        self.set_parameter_value("cutoff", value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_detune(self, value: float):
        self.set_parameter_value("detune", value)

    def set_env_curve(self, value: float):
        self.set_parameter_value(ENV_CURVE.name, value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_cutoff(self, value: float):
        self.set_parameter_value("cutoff", value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_depth(self, value: float):
        self.set_parameter_value("depth", value)

    def set_divisor(self, value: float):
        self.set_parameter_value("divisor", value)

    def set_env_curve(self, value: float):
        self.set_parameter_value(ENV_CURVE.name, value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_cutoff(self, value: float):
        self.set_parameter_value("cutoff", value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_depth(self, value: float):
        self.set_parameter_value("depth", value)

    def set_divisor(self, value: float):
        self.set_parameter_value("divisor", value)

    def set_env_curve(self, value: float):
        self.set_parameter_value(ENV_CURVE.name, value)

    def set_mod_invert_wave(self, value: float):
        self.set_parameter_value("mod_invert_wave", value)

    def set_mod_phase(self, value: float):
        self.set_parameter_value("mod_phase", value)

    def set_mod_phase_offset(self, value: float):
        self.set_parameter_value("mod_phase_offset", value)

    def set_mod_pulse_width(self, value: float):
        self.set_parameter_value("mod_pulse_width", value)

    def set_mod_range(self, value: float):
        self.set_parameter_value("mod_range", value)

    def set_mod_wave(self, value: float):
        self.set_parameter_value("mod_wave", value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_cutoff(self, value: float):
        self.set_parameter_value("cutoff", value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_env_curve(self, value: float):
        self.set_parameter_value(ENV_CURVE.name, value)

    def set_mod_invert_wave(self, value: float):
        self.set_parameter_value("mod_invert_wave", value)

    def set_mod_phase(self, value: float):
        self.set_parameter_value("mod_phase", value)

    def set_mod_phase_offset(self, value: float):
        self.set_parameter_value("mod_phase_offset", value)

    def set_mod_pulse_width(self, value: float):
        self.set_parameter_value("mod_pulse_width", value)

    def set_mod_range(self, value: float):
        self.set_parameter_value("mod_range", value)

    def set_mod_wave(self, value: float):
        self.set_parameter_value("mod_wave", value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_cutoff(self, value: float):
        self.set_parameter_value("cutoff", value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_detune(self, value: float):
        self.set_parameter_value("detune", value)

    def set_env_curve(self, value: float):
        self.set_parameter_value(ENV_CURVE.name, value)

    def set_mod_invert_wave(self, value: float):
        self.set_parameter_value("mod_invert_wave", value)

    def set_mod_phase(self, value: float):
        self.set_parameter_value("mod_phase", value)

    def set_mod_phase_offset(self, value: float):
        self.set_parameter_value("mod_phase_offset", value)

    def set_mod_pulse_width(self, value: float):
        self.set_parameter_value("mod_pulse_width", value)

    def set_mod_range(self, value: float):
        self.set_parameter_value("mod_range", value)

    def set_mod_wave(self, value: float):
        self.set_parameter_value("mod_wave", value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_cutoff(self, value: float):
        self.set_parameter_value("cutoff", value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_env_curve(self, value: float):
        self.set_parameter_value(ENV_CURVE.name, value)

    def set_mod_invert_wave(self, value: float):
        self.set_parameter_value("mod_invert_wave", value)

    def set_mod_phase(self, value: float):
        self.set_parameter_value("mod_phase", value)

    def set_mod_phase_offset(self, value: float):
        self.set_parameter_value("mod_phase_offset", value)

    def set_mod_pulse_width(self, value: float):
        self.set_parameter_value("mod_pulse_width", value)

    def set_mod_range(self, value: float):
        self.set_parameter_value("mod_range", value)

    def set_mod_wave(self, value: float):
        self.set_parameter_value("mod_wave", value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_cutoff(self, value: float):
        self.set_parameter_value("cutoff", value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_env_curve(self, value: float):
        self.set_parameter_value(ENV_CURVE.name, value)

    def set_mod_invert_wave(self, value: float):
        self.set_parameter_value("mod_invert_wave", value)

    def set_mod_phase(self, value: float):
        self.set_parameter_value("mod_phase", value)

    def set_mod_phase_offset(self, value: float):
        self.set_parameter_value("mod_phase_offset", value)

    def set_mod_pulse_width(self, value: float):
        self.set_parameter_value("mod_pulse_width", value)

    def set_mod_range(self, value: float):
        self.set_parameter_value("mod_range", value)

    def set_mod_wave(self, value: float):
        self.set_parameter_value("mod_wave", value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_cutoff(self, value: float):
        self.set_parameter_value("cutoff", value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_env_curve(self, value: float):
        self.set_parameter_value(ENV_CURVE.name, value)

    def set_mod_invert_wave(self, value: float):
        self.set_parameter_value("mod_invert_wave", value)

    def set_mod_phase(self, value: float):
        self.set_parameter_value("mod_phase", value)

    def set_mod_phase_offset(self, value: float):
        self.set_parameter_value("mod_phase_offset", value)

    def set_mod_pulse_width(self, value: float):
        self.set_parameter_value("mod_pulse_width", value)

    def set_mod_range(self, value: float):
        self.set_parameter_value("mod_range", value)

    def set_mod_wave(self, value: float):
        self.set_parameter_value("mod_wave", value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_cutoff(self, value: float):
        self.set_parameter_value("cutoff", value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_env_curve(self, value: float):
        self.set_parameter_value(ENV_CURVE.name, value)

    def set_mod_invert_wave(self, value: float):
        self.set_parameter_value("mod_invert_wave", value)

    def set_mod_phase(self, value: float):
        self.set_parameter_value("mod_phase", value)

    def set_mod_phase_offset(self, value: float):
        self.set_parameter_value("mod_phase_offset", value)

    def set_mod_pulse_width(self, value: float):
        self.set_parameter_value("mod_pulse_width", value)

    def set_mod_range(self, value: float):
        self.set_parameter_value("mod_range", value)

    def set_mod_wave(self, value: float):
        self.set_parameter_value("mod_wave", value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_pulse_width(self, value: float):
        self.set_parameter_value("pulse_width", value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_cutoff(self, value: float):
        self.set_parameter_value("cutoff", value)

    def set_cutoff_attack(self, value: float):
        self.set_parameter_value("cutoff_attack", value)

    def set_cutoff_attack_level(self, value: float):
        self.set_parameter_value("cutoff_attack_level", value)

    def set_cutoff_decay(self, value: float):
        self.set_parameter_value("cutoff_decay", value)

    def set_cutoff_decay_level(self, value: float):
        self.set_parameter_value("cutoff_decay_level", value)

    def set_cutoff_min(self, value: float):
        self.set_parameter_value("cutoff_min", value)

    def set_cutoff_release(self, value: float):
        self.set_parameter_value("cutoff_release", value)

    def set_cutoff_sustain(self, value: float):
        self.set_parameter_value("cutoff_sustain", value)

    def set_cutoff_sustain_level(self, value: float):
        self.set_parameter_value("cutoff_sustain_level", value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_env_curve(self, value: float):
        self.set_parameter_value(ENV_CURVE.name, value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_pulse_width(self, value: float):
        self.set_parameter_value("pulse_width", value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_res(self, value: float):
        self.set_parameter_value("res", value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)

    def set_wave(self, value: float):
        self.set_parameter_value("wave", value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_cutoff(self, value: float):
        self.set_parameter_value("cutoff", value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_env_curve(self, value: float):
        self.set_parameter_value(ENV_CURVE.name, value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_res(self, value: float):
        self.set_parameter_value("res", value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_cutoff(self, value: float):
        self.set_parameter_value("cutoff", value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_env_curve(self, value: float):
        self.set_parameter_value(ENV_CURVE.name, value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_res(self, value: float):
        self.set_parameter_value("res", value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_cutoff(self, value: float):
        self.set_parameter_value("cutoff", value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_env_curve(self, value: float):
        self.set_parameter_value(ENV_CURVE.name, value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_res(self, value: float):
        self.set_parameter_value("res", value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_cutoff(self, value: float):
        self.set_parameter_value("cutoff", value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_disable_wave(self, value: float):
        self.set_parameter_value("disable_wave", value)

    def set_env_curve(self, value: float):
        self.set_parameter_value(ENV_CURVE.name, value)

    def set_invert_wave(self, value: float):
        self.set_parameter_value("invert_wave", value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_phase(self, value: float):
        self.set_parameter_value("phase", value)

    def set_phase_offset(self, value: float):
        self.set_parameter_value("phase_offset", value)

    def set_pulse_width(self, value: float):
        self.set_parameter_value("pulse_width", value)

    def set_range(self, value: float):
        self.set_parameter_value("range", value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_res(self, value: float):
        self.set_parameter_value("res", value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)

    def set_wave(self, value: float):
        self.set_parameter_value("wave", value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_cutoff(self, value: float):
        self.set_parameter_value("cutoff", value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_detune1(self, value: float):
        self.set_parameter_value("detune1", value)

    def set_detune2(self, value: float):
        self.set_parameter_value("detune2", value)

    def set_env_curve(self, value: float):
        self.set_parameter_value(ENV_CURVE.name, value)

    def set_noise(self, value: float):
        self.set_parameter_value("noise", value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_res(self, value: float):
        self.set_parameter_value("res", value)

    def set_reverb_time(self, value: float):
        self.set_parameter_value("reverb_time", value)

    def set_ring(self, value: float):
        self.set_parameter_value("ring", value)

    def set_room(self, value: float):
        self.set_parameter_value("room", value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_cutoff(self, value: float):
        self.set_parameter_value("cutoff", value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_env_curve(self, value: float):
        self.set_parameter_value(ENV_CURVE.name, value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_res(self, value: float):
        self.set_parameter_value("res", value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_cutoff(self, value: float):
        self.set_parameter_value("cutoff", value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_env_curve(self, value: float):
        self.set_parameter_value(ENV_CURVE.name, value)

    def set_noise(self, value: float):
        self.set_parameter_value("noise", value)

    def set_norm(self, value: float):
        self.set_parameter_value("norm", value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_res(self, value: float):
        self.set_parameter_value("res", value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_clamp_time(self, value: float):
        self.set_parameter_value("clamp_time", value)

    def set_compress(self, value: float):
        self.set_parameter_value("compress", value)

    def set_cutoff(self, value: float):
        self.set_parameter_value("cutoff", value)

    def set_cutoff_attack(self, value: float):
        self.set_parameter_value("cutoff_attack", value)

    def set_cutoff_attack_level(self, value: float):
        self.set_parameter_value("cutoff_attack_level", value)

    def set_cutoff_decay(self, value: float):
        self.set_parameter_value("cutoff_decay", value)

    def set_cutoff_decay_level(self, value: float):
        self.set_parameter_value("cutoff_decay_level", value)

    def set_cutoff_env_curve(self, value: float):
        self.set_parameter_value("cutoff_env_curve", value)

    def set_cutoff_min(self, value: float):
        self.set_parameter_value("cutoff_min", value)

    def set_cutoff_release(self, value: float):
        self.set_parameter_value("cutoff_release", value)

    def set_cutoff_sustain(self, value: float):
        self.set_parameter_value("cutoff_sustain", value)

    def set_cutoff_sustain_level(self, value: float):
        self.set_parameter_value("cutoff_sustain_level", value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_env_curve(self, value: float):
        self.set_parameter_value(ENV_CURVE.name, value)

    def set_finish(self, value: float):
        self.set_parameter_value("finish", value)

    def set_norm(self, value: float):
        self.set_parameter_value("norm", value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_pitch(self, value: float):
        self.set_parameter_value("pitch", value)

    def set_pitch_dis(self, value: float):
        self.set_parameter_value("pitch_dis", value)

    def set_pre_amp(self, value: float):
        self.set_parameter_value("pre_amp", value)

    def set_rate(self, value: float):
        self.set_parameter_value("rate", value)

    def set_relax_time(self, value: float):
        self.set_parameter_value("relax_time", value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_res(self, value: float):
        self.set_parameter_value("res", value)

    def set_slope_above(self, value: float):
        self.set_parameter_value("slope_above", value)

    def set_slope_below(self, value: float):
        self.set_parameter_value("slope_below", value)

    def set_start(self, value: float):
        self.set_parameter_value("start", value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)

    def set_threshold(self, value: float):
        self.set_parameter_value("threshold", value)

    def set_time_dis(self, value: float):
        self.set_parameter_value("time_dis", value)

    def set_window_size(self, value: float):
        self.set_parameter_value("window_size", value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_cutoff(self, value: float):
        self.set_parameter_value("cutoff", value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_env_curve(self, value: float):
        self.set_parameter_value(ENV_CURVE.name, value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)

    def set_vibrato_delay(self, value: float):
        self.set_parameter_value("vibrato_delay", value)

    def set_vibrato_depth(self, value: float):
        self.set_parameter_value("vibrato_depth", value)

    def set_vibrato_onset(self, value: float):
        self.set_parameter_value("vibrato_onset", value)

    def set_vibrato_rate(self, value: float):
        self.set_parameter_value("vibrato_rate", value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_hard(self, value: float):
        self.set_parameter_value("hard", value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_stereo_width(self, value: float):
        self.set_parameter_value("stereo_width", value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)

    def set_vel(self, value: float):
        self.set_parameter_value("vel", value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_coef(self, value: float):
        self.set_parameter_value("coef", value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_max_delay_time(self, value: float):
        self.set_parameter_value("max_delay_time", value)

    def set_noise_amp(self, value: float):
        self.set_parameter_value("noise_amp", value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_pluck_decay(self, value: float):
        self.set_parameter_value("pluck_decay", value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)


class SoundIn(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [AMP, PAN, SynthParameterDefinition(name="input", default_value=0.0)]

    def get_ruby_synth_name(self) -> str:
        return "sound_in"


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_input(self, value: float):
        self.set_parameter_value("input", value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_cutoff(self, value: float):
        self.set_parameter_value("cutoff", value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_env_curve(self, value: float):
        self.set_parameter_value(ENV_CURVE.name, value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_res(self, value: float):
        self.set_parameter_value("res", value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_cutoff(self, value: float):
        self.set_parameter_value("cutoff", value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_env_curve(self, value: float):
        self.set_parameter_value(ENV_CURVE.name, value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_res(self, value: float):
        self.set_parameter_value("res", value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_cutoff(self, value: float):
        self.set_parameter_value("cutoff", value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_env_curve(self, value: float):
        self.set_parameter_value(ENV_CURVE.name, value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_res(self, value: float):
        self.set_parameter_value("res", value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_cutoff(self, value: float):
        self.set_parameter_value("cutoff", value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_env_curve(self, value: float):
        self.set_parameter_value(ENV_CURVE.name, value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_res(self, value: float):
        self.set_parameter_value("res", value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_attack(self, value: float):
        self.set_parameter_value(ATTACK.name, value)

    def set_attack_level(self, value: float):
        self.set_parameter_value(ATTACK_LEVEL.name, value)

    def set_cutoff(self, value: float):
        self.set_parameter_value("cutoff", value)

    def set_decay(self, value: float):
        self.set_parameter_value(DECAY.name, value)

    def set_decay_level(self, value: float):
        self.set_parameter_value(DECAY_LEVEL.name, value)

    def set_env_curve(self, value: float):
        self.set_parameter_value(ENV_CURVE.name, value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_release(self, value: float):
        self.set_parameter_value(RELEASE.name, value)

    def set_res(self, value: float):
        self.set_parameter_value("res", value)

    def set_sustain(self, value: float):
        self.set_parameter_value(SUSTAIN.name, value)

    def set_sustain_level(self, value: float):
        self.set_parameter_value(SUSTAIN_LEVEL.name, value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_cutoff(self, value: float):
        self.set_parameter_value("cutoff", value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_rate(self, value: float):
        self.set_parameter_value("rate", value)

    def set_res(self, value: float):
        self.set_parameter_value("res", value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_cutoff(self, value: float):
        self.set_parameter_value("cutoff", value)

    def set_pan(self, value: float):
        self.set_parameter_value(PAN.name, value)

    def set_rate(self, value: float):
        self.set_parameter_value("rate", value)

    def set_res(self, value: float):
        self.set_parameter_value("res", value)


class BasicMixer(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [AMP]

    def get_ruby_synth_name(self) -> str:
        return "basic_mixer"


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)


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


    def set_amp(self, value: float):
        self.set_parameter_value(AMP.name, value)

    def set_force_mono(self, value: float):
        self.set_parameter_value("force_mono", value)

    def set_hpf(self, value: float):
        self.set_parameter_value("hpf", value)

    def set_hpf_bypass(self, value: float):
        self.set_parameter_value("hpf_bypass", value)

    def set_invert_stereo(self, value: float):
        self.set_parameter_value("invert_stereo", value)

    def set_leak_dc_bypass(self, value: float):
        self.set_parameter_value("leak_dc_bypass", value)

    def set_limiter_bypass(self, value: float):
        self.set_parameter_value("limiter_bypass", value)

    def set_lpf(self, value: float):
        self.set_parameter_value("lpf", value)

    def set_lpf_bypass(self, value: float):
        self.set_parameter_value("lpf_bypass", value)

    def set_pre_amp(self, value: float):
        self.set_parameter_value("pre_amp", value)
