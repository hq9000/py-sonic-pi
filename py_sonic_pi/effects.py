from py_sonic_pi.inventory import EffectInstance, SlideShape


class HPFilter(EffectInstance):
    cutoff: float = 0.0
    cutoff_slide: float = 0.0

    def __init__(
        self,
        id: str,
        cutoff: float = 0.0,
        cutoff_slide: float = 0.0,
        controllable: bool = False,
    ):
        super().__init__(id=id, controllable=controllable)
        self.cutoff = cutoff
        self.cutoff_slide = cutoff_slide

    def get_ruby_effect_name(self) -> str:
        return "rhpf"

    def get_fx_params_dict(self) -> dict[str, float]:
        return {"cutoff": self.cutoff, "cutoff_slide": self.cutoff_slide}

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
        return {"amp": self.gain}

    def get_param_names(self):
        return ["amp"]


class Panner(EffectInstance):
    pan: float = 0.0
    pan_slide: float = 0.0
    pan_slide_shape: SlideShape = SlideShape.LINEAR

    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR

    def __init__(
        self,
        id: str,
        pan: float,
        pan_slide: float,
        pan_slide_shape: SlideShape,
        amp: float,
        amp_slide: float,
        amp_slide_shape: SlideShape,
        controllable: bool,
    ):
        super().__init__(id=id, controllable=controllable)
        self.amp = amp
        self.amp_slide = amp_slide
        self.amp_slide_shape = amp_slide_shape

        self.pan = pan
        self.pan_slide = pan_slide
        self.pan_slide_shape = pan_slide_shape

    def get_ruby_effect_name(self) -> str:
        return "pan"

    def get_fx_params_dict(self) -> dict[str, float]:
        return {
            "pan": self.pan,
            "amp": self.amp,
            "amp_slide": self.amp_slide,
            "amp_slide_shape": self.amp_slide_shape.value,
            "pan": self.pan,
            "pan_slide": self.pan_slide,
            "pan_slide_shape": self.pan_slide_shape.value,
        }

    def get_param_names(self):
        return ["pan"]
