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


class Gain(EffectInstance):
    gain: float = 1.0

    def __init__(self, id: str, gain: float = 1.0, controllable: bool = False):
        super().__init__(id=id, controllable=controllable)
        self.gain = gain

    def get_ruby_effect_name(self) -> str:
        return "level"

    def get_fx_params_dict(self) -> dict[str, float]:
        return {"amp": self.gain}


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


class Reverb(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 0.5
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 0.5
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    room: float = 0.5
    room_slide: float = 0.0
    room_slide_shape: SlideShape = SlideShape.LINEAR
    damp: float = 0.5
    damp_slide: float = 0.0
    damp_slide_shape: SlideShape = SlideShape.LINEAR

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 0.5,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 0.5,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        room: float = 0.5,
        room_slide: float = 0.0,
        room_slide_shape: SlideShape = SlideShape.LINEAR,
        damp: float = 0.5,
        damp_slide: float = 0.0,
        damp_slide_shape: SlideShape = SlideShape.LINEAR,
        controllable: bool = False,
    ):
        super().__init__(id=id, controllable=controllable)
        self.amp = amp
        self.amp_slide = amp_slide
        self.amp_slide_shape = amp_slide_shape
        self.mix = mix
        self.mix_slide = mix_slide
        self.mix_slide_shape = mix_slide_shape
        self.pre_mix = pre_mix
        self.pre_mix_slide = pre_mix_slide
        self.pre_mix_slide_shape = pre_mix_slide_shape
        self.pre_amp = pre_amp
        self.pre_amp_slide = pre_amp_slide
        self.pre_amp_slide_shape = pre_amp_slide_shape
        self.room = room
        self.room_slide = room_slide
        self.room_slide_shape = room_slide_shape
        self.damp = damp
        self.damp_slide = damp_slide
        self.damp_slide_shape = damp_slide_shape

    def get_ruby_effect_name(self) -> str:
        return "reverb"

    def get_fx_params_dict(self) -> dict[str, float]:
        return {
            "amp": self.amp,
            "amp_slide": self.amp_slide,
            "amp_slide_shape": self.amp_slide_shape.value,
            "mix": self.mix,
            "mix_slide": self.mix_slide,
            "mix_slide_shape": self.mix_slide_shape.value,
            "pre_mix": self.pre_mix,
            "pre_mix_slide": self.pre_mix_slide,
            "pre_mix_slide_shape": self.pre_mix_slide_shape.value,
            "pre_amp": self.pre_amp,
            "pre_amp_slide": self.pre_amp_slide,
            "pre_amp_slide_shape": self.pre_amp_slide_shape.value,
            "room": self.room,
            "room_slide": self.room_slide,
            "room_slide_shape": self.room_slide_shape.value,
            "damp": self.damp,
            "damp_slide": self.damp_slide,
            "damp_slide_shape": self.damp_slide_shape.value,
        }
