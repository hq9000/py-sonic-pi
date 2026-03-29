from py_sonic_pi.inventory import EffectInstance


class HPFilter(EffectInstance):
    cutoff: float = 0.0
    cutoff_slide: float = 0.0

    def __init__(self, id: str, cutoff: float = 0.0, cutoff_slide: float = 0.0, controllable: bool = False):
        super().__init__(id=id, controllable=controllable)
        self.cutoff = cutoff
        self.cutoff_slide = cutoff_slide

    def get_ruby_effect_name(self) -> str:
        return "rhpf"

    def get_fx_params_dict(self) -> dict[str, float]:
        return {
            "cutoff": self.cutoff,
            "cutoff_slide": self.cutoff_slide
        }

    def get_param_names(self):
        return ["cutoff", "cutoff_slide"]


class Gain(EffectInstance):
    gain: float = 1.0

    def __init__(self, id: str, gain: float = 1.0, controllable: bool = False):
        super().__init__(id=id, controllable=controllable)
        self.gain = gain

    def get_ruby_effect_name(self) -> str:
        return "level"

    def get_fx_params_dict(self) -> dict[str, float]:
        return {
            "amp": self.gain
        }

    def get_param_names(self):
        return ["amp"]