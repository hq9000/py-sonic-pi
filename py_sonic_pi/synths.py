from py_sonic_pi.inventory import Synth, SynthParameterDefinition

AMP = SynthParameterDefinition(
    name="amp",
    default_value=1.0,
    min_value=0.0,
    max_value=10.0,
)


class Tb303(Synth):
    def get_parameters_definitions(self) -> list[SynthParameterDefinition]:
        return [
            AMP,
            SynthParameterDefinition(
                name="cutoff",
                default_value=100,
                min_value=0,
                max_value=130,
            ),
        ]

    def get_ruby_synth_name(self) -> str:
        return "tb303"
