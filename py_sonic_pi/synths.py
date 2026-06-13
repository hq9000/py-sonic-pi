from py_sonic_pi.inventory import Synth, SynthParameter

AMP = SynthParameter(
    name="amp",
    default_value=1.0,
    min_value=0.0,
    max_value=10.0,
)

class Tb303(Synth):

    def get_synth_parameters(self) -> list[SynthParameter]:
        return [
            AMP,
            SynthParameter(
                name="cutoff",
                default_value=100,
                min_value=0,
                max_value=130,
            )
        ]

    def get_ruby_synth_name(self) -> str:
        return "tb303"
