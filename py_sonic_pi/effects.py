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


class EQ(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    low_shelf: float = 0.0
    low_shelf_slide: float = 0.0
    low_shelf_slide_shape: SlideShape = SlideShape.LINEAR
    low_shelf_note: float = 43.349957
    low_shelf_note_slide: float = 0.0
    low_shelf_note_slide_shape: SlideShape = SlideShape.LINEAR
    low_shelf_slope: float = 1.0
    low_shelf_slope_slide: float = 0.0
    low_shelf_slope_slide_shape: SlideShape = SlideShape.LINEAR
    low: float = 0.0
    low_slide: float = 0.0
    low_slide_shape: SlideShape = SlideShape.LINEAR
    low_note: float = 59.2130948
    low_note_slide: float = 0.0
    low_note_slide_shape: SlideShape = SlideShape.LINEAR
    low_q: float = 0.6
    low_q_slide: float = 0.0
    low_q_slide_shape: SlideShape = SlideShape.LINEAR
    mid: float = 0.0
    mid_slide: float = 0.0
    mid_slide_shape: SlideShape = SlideShape.LINEAR
    mid_note: float = 83.2130948
    mid_note_slide: float = 0.0
    mid_note_slide_shape: SlideShape = SlideShape.LINEAR
    mid_q: float = 0.6
    mid_q_slide: float = 0.0
    mid_q_slide_shape: SlideShape = SlideShape.LINEAR
    high: float = 0.0
    high_slide: float = 0.0
    high_slide_shape: SlideShape = SlideShape.LINEAR
    high_note: float = 104.9013539
    high_note_slide: float = 0.0
    high_note_slide_shape: SlideShape = SlideShape.LINEAR
    high_q: float = 0.6
    high_q_slide: float = 0.0
    high_q_slide_shape: SlideShape = SlideShape.LINEAR
    high_shelf: float = 0.0
    high_shelf_slide: float = 0.0
    high_shelf_slide_shape: SlideShape = SlideShape.LINEAR
    high_shelf_note: float = 114.2326448
    high_shelf_note_slide: float = 0.0
    high_shelf_note_slide_shape: SlideShape = SlideShape.LINEAR
    high_shelf_slope: float = 1.0
    high_shelf_slope_slide: float = 0.0
    high_shelf_slope_slide_shape: SlideShape = SlideShape.LINEAR

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        low_shelf: float = 0.0,
        low_shelf_slide: float = 0.0,
        low_shelf_slide_shape: SlideShape = SlideShape.LINEAR,
        low_shelf_note: float = 43.349957,
        low_shelf_note_slide: float = 0.0,
        low_shelf_note_slide_shape: SlideShape = SlideShape.LINEAR,
        low_shelf_slope: float = 1.0,
        low_shelf_slope_slide: float = 0.0,
        low_shelf_slope_slide_shape: SlideShape = SlideShape.LINEAR,
        low: float = 0.0,
        low_slide: float = 0.0,
        low_slide_shape: SlideShape = SlideShape.LINEAR,
        low_note: float = 59.2130948,
        low_note_slide: float = 0.0,
        low_note_slide_shape: SlideShape = SlideShape.LINEAR,
        low_q: float = 0.6,
        low_q_slide: float = 0.0,
        low_q_slide_shape: SlideShape = SlideShape.LINEAR,
        mid: float = 0.0,
        mid_slide: float = 0.0,
        mid_slide_shape: SlideShape = SlideShape.LINEAR,
        mid_note: float = 83.2130948,
        mid_note_slide: float = 0.0,
        mid_note_slide_shape: SlideShape = SlideShape.LINEAR,
        mid_q: float = 0.6,
        mid_q_slide: float = 0.0,
        mid_q_slide_shape: SlideShape = SlideShape.LINEAR,
        high: float = 0.0,
        high_slide: float = 0.0,
        high_slide_shape: SlideShape = SlideShape.LINEAR,
        high_note: float = 104.9013539,
        high_note_slide: float = 0.0,
        high_note_slide_shape: SlideShape = SlideShape.LINEAR,
        high_q: float = 0.6,
        high_q_slide: float = 0.0,
        high_q_slide_shape: SlideShape = SlideShape.LINEAR,
        high_shelf: float = 0.0,
        high_shelf_slide: float = 0.0,
        high_shelf_slide_shape: SlideShape = SlideShape.LINEAR,
        high_shelf_note: float = 114.2326448,
        high_shelf_note_slide: float = 0.0,
        high_shelf_note_slide_shape: SlideShape = SlideShape.LINEAR,
        high_shelf_slope: float = 1.0,
        high_shelf_slope_slide: float = 0.0,
        high_shelf_slope_slide_shape: SlideShape = SlideShape.LINEAR,
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
        self.low_shelf = low_shelf
        self.low_shelf_slide = low_shelf_slide
        self.low_shelf_slide_shape = low_shelf_slide_shape
        self.low_shelf_note = low_shelf_note
        self.low_shelf_note_slide = low_shelf_note_slide
        self.low_shelf_note_slide_shape = low_shelf_note_slide_shape
        self.low_shelf_slope = low_shelf_slope
        self.low_shelf_slope_slide = low_shelf_slope_slide
        self.low_shelf_slope_slide_shape = low_shelf_slope_slide_shape
        self.low = low
        self.low_slide = low_slide
        self.low_slide_shape = low_slide_shape
        self.low_note = low_note
        self.low_note_slide = low_note_slide
        self.low_note_slide_shape = low_note_slide_shape
        self.low_q = low_q
        self.low_q_slide = low_q_slide
        self.low_q_slide_shape = low_q_slide_shape
        self.mid = mid
        self.mid_slide = mid_slide
        self.mid_slide_shape = mid_slide_shape
        self.mid_note = mid_note
        self.mid_note_slide = mid_note_slide
        self.mid_note_slide_shape = mid_note_slide_shape
        self.mid_q = mid_q
        self.mid_q_slide = mid_q_slide
        self.mid_q_slide_shape = mid_q_slide_shape
        self.high = high
        self.high_slide = high_slide
        self.high_slide_shape = high_slide_shape
        self.high_note = high_note
        self.high_note_slide = high_note_slide
        self.high_note_slide_shape = high_note_slide_shape
        self.high_q = high_q
        self.high_q_slide = high_q_slide
        self.high_q_slide_shape = high_q_slide_shape
        self.high_shelf = high_shelf
        self.high_shelf_slide = high_shelf_slide
        self.high_shelf_slide_shape = high_shelf_slide_shape
        self.high_shelf_note = high_shelf_note
        self.high_shelf_note_slide = high_shelf_note_slide
        self.high_shelf_note_slide_shape = high_shelf_note_slide_shape
        self.high_shelf_slope = high_shelf_slope
        self.high_shelf_slope_slide = high_shelf_slope_slide
        self.high_shelf_slope_slide_shape = high_shelf_slope_slide_shape

    def get_ruby_effect_name(self) -> str:
        return "eq"

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
            "low_shelf": self.low_shelf,
            "low_shelf_slide": self.low_shelf_slide,
            "low_shelf_slide_shape": self.low_shelf_slide_shape.value,
            "low_shelf_note": self.low_shelf_note,
            "low_shelf_note_slide": self.low_shelf_note_slide,
            "low_shelf_note_slide_shape": self.low_shelf_note_slide_shape.value,
            "low_shelf_slope": self.low_shelf_slope,
            "low_shelf_slope_slide": self.low_shelf_slope_slide,
            "low_shelf_slope_slide_shape": self.low_shelf_slope_slide_shape.value,
            "low": self.low,
            "low_slide": self.low_slide,
            "low_slide_shape": self.low_slide_shape.value,
            "low_note": self.low_note,
            "low_note_slide": self.low_note_slide,
            "low_note_slide_shape": self.low_note_slide_shape.value,
            "low_q": self.low_q,
            "low_q_slide": self.low_q_slide,
            "low_q_slide_shape": self.low_q_slide_shape.value,
            "mid": self.mid,
            "mid_slide": self.mid_slide,
            "mid_slide_shape": self.mid_slide_shape.value,
            "mid_note": self.mid_note,
            "mid_note_slide": self.mid_note_slide,
            "mid_note_slide_shape": self.mid_note_slide_shape.value,
            "mid_q": self.mid_q,
            "mid_q_slide": self.mid_q_slide,
            "mid_q_slide_shape": self.mid_q_slide_shape.value,
            "high": self.high,
            "high_slide": self.high_slide,
            "high_slide_shape": self.high_slide_shape.value,
            "high_note": self.high_note,
            "high_note_slide": self.high_note_slide,
            "high_note_slide_shape": self.high_note_slide_shape.value,
            "high_q": self.high_q,
            "high_q_slide": self.high_q_slide,
            "high_q_slide_shape": self.high_q_slide_shape.value,
            "high_shelf": self.high_shelf,
            "high_shelf_slide": self.high_shelf_slide,
            "high_shelf_slide_shape": self.high_shelf_slide_shape.value,
            "high_shelf_note": self.high_shelf_note,
            "high_shelf_note_slide": self.high_shelf_note_slide,
            "high_shelf_note_slide_shape": self.high_shelf_note_slide_shape.value,
            "high_shelf_slope": self.high_shelf_slope,
            "high_shelf_slope_slide": self.high_shelf_slope_slide,
            "high_shelf_slope_slide_shape": self.high_shelf_slope_slide_shape.value,
        }


class GVerb(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    spread: float = 0.5
    spread_slide: float = 0.0
    spread_slide_shape: SlideShape = SlideShape.LINEAR
    damp: float = 0.5
    damp_slide: float = 0.0
    damp_slide_shape: SlideShape = SlideShape.LINEAR
    pre_damp: float = 0.5
    pre_damp_slide: float = 0.0
    pre_damp_slide_shape: SlideShape = SlideShape.LINEAR
    dry: float = 1.0
    dry_slide: float = 0.0
    dry_slide_shape: SlideShape = SlideShape.LINEAR
    room: float = 10.0
    release: float = 3.0
    ref_level: float = 0.7
    tail_level: float = 0.5

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        spread: float = 0.5,
        spread_slide: float = 0.0,
        spread_slide_shape: SlideShape = SlideShape.LINEAR,
        damp: float = 0.5,
        damp_slide: float = 0.0,
        damp_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_damp: float = 0.5,
        pre_damp_slide: float = 0.0,
        pre_damp_slide_shape: SlideShape = SlideShape.LINEAR,
        dry: float = 1.0,
        dry_slide: float = 0.0,
        dry_slide_shape: SlideShape = SlideShape.LINEAR,
        room: float = 10.0,
        release: float = 3.0,
        ref_level: float = 0.7,
        tail_level: float = 0.5,
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
        self.spread = spread
        self.spread_slide = spread_slide
        self.spread_slide_shape = spread_slide_shape
        self.damp = damp
        self.damp_slide = damp_slide
        self.damp_slide_shape = damp_slide_shape
        self.pre_damp = pre_damp
        self.pre_damp_slide = pre_damp_slide
        self.pre_damp_slide_shape = pre_damp_slide_shape
        self.dry = dry
        self.dry_slide = dry_slide
        self.dry_slide_shape = dry_slide_shape
        self.room = room
        self.release = release
        self.ref_level = ref_level
        self.tail_level = tail_level

    def get_ruby_effect_name(self) -> str:
        return "gverb"

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
            "spread": self.spread,
            "spread_slide": self.spread_slide,
            "spread_slide_shape": self.spread_slide_shape.value,
            "damp": self.damp,
            "damp_slide": self.damp_slide,
            "damp_slide_shape": self.damp_slide_shape.value,
            "pre_damp": self.pre_damp,
            "pre_damp_slide": self.pre_damp_slide,
            "pre_damp_slide_shape": self.pre_damp_slide_shape.value,
            "dry": self.dry,
            "dry_slide": self.dry_slide,
            "dry_slide_shape": self.dry_slide_shape.value,
            "room": self.room,
            "release": self.release,
            "ref_level": self.ref_level,
            "tail_level": self.tail_level,
        }


class Krush(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    gain: float = 5.0
    gain_slide: float = 0.0
    gain_slide_shape: SlideShape = SlideShape.LINEAR
    cutoff: float = 100.0
    cutoff_slide: float = 0.0
    cutoff_slide_shape: SlideShape = SlideShape.LINEAR
    res: float = 0.0
    res_slide: float = 0.0
    res_slide_shape: SlideShape = SlideShape.LINEAR

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        gain: float = 5.0,
        gain_slide: float = 0.0,
        gain_slide_shape: SlideShape = SlideShape.LINEAR,
        cutoff: float = 100.0,
        cutoff_slide: float = 0.0,
        cutoff_slide_shape: SlideShape = SlideShape.LINEAR,
        res: float = 0.0,
        res_slide: float = 0.0,
        res_slide_shape: SlideShape = SlideShape.LINEAR,
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
        self.gain = gain
        self.gain_slide = gain_slide
        self.gain_slide_shape = gain_slide_shape
        self.cutoff = cutoff
        self.cutoff_slide = cutoff_slide
        self.cutoff_slide_shape = cutoff_slide_shape
        self.res = res
        self.res_slide = res_slide
        self.res_slide_shape = res_slide_shape

    def get_ruby_effect_name(self) -> str:
        return "krush"

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
            "gain": self.gain,
            "gain_slide": self.gain_slide,
            "gain_slide_shape": self.gain_slide_shape.value,
            "cutoff": self.cutoff,
            "cutoff_slide": self.cutoff_slide,
            "cutoff_slide_shape": self.cutoff_slide_shape.value,
            "res": self.res,
            "res_slide": self.res_slide,
            "res_slide_shape": self.res_slide_shape.value,
        }


class Bitcrusher(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    sample_rate: float = 10000.0
    sample_rate_slide: float = 0.0
    sample_rate_slide_shape: SlideShape = SlideShape.LINEAR
    bits: float = 8.0
    bits_slide: float = 0.0
    bits_slide_shape: SlideShape = SlideShape.LINEAR
    cutoff: float = 0.0
    cutoff_slide: float = 0.0
    cutoff_slide_shape: SlideShape = SlideShape.LINEAR

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        sample_rate: float = 10000.0,
        sample_rate_slide: float = 0.0,
        sample_rate_slide_shape: SlideShape = SlideShape.LINEAR,
        bits: float = 8.0,
        bits_slide: float = 0.0,
        bits_slide_shape: SlideShape = SlideShape.LINEAR,
        cutoff: float = 0.0,
        cutoff_slide: float = 0.0,
        cutoff_slide_shape: SlideShape = SlideShape.LINEAR,
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
        self.sample_rate = sample_rate
        self.sample_rate_slide = sample_rate_slide
        self.sample_rate_slide_shape = sample_rate_slide_shape
        self.bits = bits
        self.bits_slide = bits_slide
        self.bits_slide_shape = bits_slide_shape
        self.cutoff = cutoff
        self.cutoff_slide = cutoff_slide
        self.cutoff_slide_shape = cutoff_slide_shape

    def get_ruby_effect_name(self) -> str:
        return "bitcrusher"

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
            "sample_rate": self.sample_rate,
            "sample_rate_slide": self.sample_rate_slide,
            "sample_rate_slide_shape": self.sample_rate_slide_shape.value,
            "bits": self.bits,
            "bits_slide": self.bits_slide,
            "bits_slide_shape": self.bits_slide_shape.value,
            "cutoff": self.cutoff,
            "cutoff_slide": self.cutoff_slide,
            "cutoff_slide_shape": self.cutoff_slide_shape.value,
        }


class Autotuner(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    note: float = 0.0
    note_slide: float = 0.0
    note_slide_shape: SlideShape = SlideShape.LINEAR
    formant_ratio: float = 1.0
    formant_ratio_slide: float = 0.0
    formant_ratio_slide_shape: SlideShape = SlideShape.LINEAR

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        note: float = 0.0,
        note_slide: float = 0.0,
        note_slide_shape: SlideShape = SlideShape.LINEAR,
        formant_ratio: float = 1.0,
        formant_ratio_slide: float = 0.0,
        formant_ratio_slide_shape: SlideShape = SlideShape.LINEAR,
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
        self.note = note
        self.note_slide = note_slide
        self.note_slide_shape = note_slide_shape
        self.formant_ratio = formant_ratio
        self.formant_ratio_slide = formant_ratio_slide
        self.formant_ratio_slide_shape = formant_ratio_slide_shape

    def get_ruby_effect_name(self) -> str:
        return "autotuner"

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
            "note": self.note,
            "note_slide": self.note_slide,
            "note_slide_shape": self.note_slide_shape.value,
            "formant_ratio": self.formant_ratio,
            "formant_ratio_slide": self.formant_ratio_slide,
            "formant_ratio_slide_shape": self.formant_ratio_slide_shape.value,
        }


class Mono(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    pan: float = 0.0
    pan_slide: float = 0.0
    pan_slide_shape: SlideShape = SlideShape.LINEAR

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        pan: float = 0.0,
        pan_slide: float = 0.0,
        pan_slide_shape: SlideShape = SlideShape.LINEAR,
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
        self.pan = pan
        self.pan_slide = pan_slide
        self.pan_slide_shape = pan_slide_shape

    def get_ruby_effect_name(self) -> str:
        return "mono"

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
            "pan": self.pan,
            "pan_slide": self.pan_slide,
            "pan_slide_shape": self.pan_slide_shape.value,
        }


class Echo(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    phase: float = 0.25
    phase_slide: float = 0.0
    phase_slide_shape: SlideShape = SlideShape.LINEAR
    decay: float = 2.0
    decay_slide: float = 0.0
    decay_slide_shape: SlideShape = SlideShape.LINEAR
    max_phase: float = 2.0

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        phase: float = 0.25,
        phase_slide: float = 0.0,
        phase_slide_shape: SlideShape = SlideShape.LINEAR,
        decay: float = 2.0,
        decay_slide: float = 0.0,
        decay_slide_shape: SlideShape = SlideShape.LINEAR,
        max_phase: float = 2.0,
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
        self.phase = phase
        self.phase_slide = phase_slide
        self.phase_slide_shape = phase_slide_shape
        self.decay = decay
        self.decay_slide = decay_slide
        self.decay_slide_shape = decay_slide_shape
        self.max_phase = max_phase

    def get_ruby_effect_name(self) -> str:
        return "echo"

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
            "phase": self.phase,
            "phase_slide": self.phase_slide,
            "phase_slide_shape": self.phase_slide_shape.value,
            "decay": self.decay,
            "decay_slide": self.decay_slide,
            "decay_slide_shape": self.decay_slide_shape.value,
            "max_phase": self.max_phase,
        }


class Slicer(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    phase: float = 0.25
    phase_slide: float = 0.0
    phase_slide_shape: SlideShape = SlideShape.LINEAR
    amp_min: float = 0.0
    amp_min_slide: float = 0.0
    amp_min_slide_shape: SlideShape = SlideShape.LINEAR
    amp_max: float = 1.0
    amp_max_slide: float = 0.0
    amp_max_slide_shape: SlideShape = SlideShape.LINEAR
    pulse_width: float = 0.5
    pulse_width_slide: float = 0.0
    pulse_width_slide_shape: SlideShape = SlideShape.LINEAR
    phase_offset: float = 0.0
    wave: float = 1.0
    invert_wave: float = 0.0
    probability: float = 0.0
    probability_slide: float = 0.0
    probability_slide_shape: SlideShape = SlideShape.LINEAR
    prob_pos: float = 0.0
    prob_pos_slide: float = 0.0
    prob_pos_slide_shape: SlideShape = SlideShape.LINEAR
    seed: float = 0.0
    smooth: float = 0.0
    smooth_slide: float = 0.0
    smooth_slide_shape: SlideShape = SlideShape.LINEAR
    smooth_up: float = 0.0
    smooth_up_slide: float = 0.0
    smooth_up_slide_shape: SlideShape = SlideShape.LINEAR
    smooth_down: float = 0.0
    smooth_down_slide: float = 0.0
    smooth_down_slide_shape: SlideShape = SlideShape.LINEAR

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        phase: float = 0.25,
        phase_slide: float = 0.0,
        phase_slide_shape: SlideShape = SlideShape.LINEAR,
        amp_min: float = 0.0,
        amp_min_slide: float = 0.0,
        amp_min_slide_shape: SlideShape = SlideShape.LINEAR,
        amp_max: float = 1.0,
        amp_max_slide: float = 0.0,
        amp_max_slide_shape: SlideShape = SlideShape.LINEAR,
        pulse_width: float = 0.5,
        pulse_width_slide: float = 0.0,
        pulse_width_slide_shape: SlideShape = SlideShape.LINEAR,
        phase_offset: float = 0.0,
        wave: float = 1.0,
        invert_wave: float = 0.0,
        probability: float = 0.0,
        probability_slide: float = 0.0,
        probability_slide_shape: SlideShape = SlideShape.LINEAR,
        prob_pos: float = 0.0,
        prob_pos_slide: float = 0.0,
        prob_pos_slide_shape: SlideShape = SlideShape.LINEAR,
        seed: float = 0.0,
        smooth: float = 0.0,
        smooth_slide: float = 0.0,
        smooth_slide_shape: SlideShape = SlideShape.LINEAR,
        smooth_up: float = 0.0,
        smooth_up_slide: float = 0.0,
        smooth_up_slide_shape: SlideShape = SlideShape.LINEAR,
        smooth_down: float = 0.0,
        smooth_down_slide: float = 0.0,
        smooth_down_slide_shape: SlideShape = SlideShape.LINEAR,
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
        self.phase = phase
        self.phase_slide = phase_slide
        self.phase_slide_shape = phase_slide_shape
        self.amp_min = amp_min
        self.amp_min_slide = amp_min_slide
        self.amp_min_slide_shape = amp_min_slide_shape
        self.amp_max = amp_max
        self.amp_max_slide = amp_max_slide
        self.amp_max_slide_shape = amp_max_slide_shape
        self.pulse_width = pulse_width
        self.pulse_width_slide = pulse_width_slide
        self.pulse_width_slide_shape = pulse_width_slide_shape
        self.phase_offset = phase_offset
        self.wave = wave
        self.invert_wave = invert_wave
        self.probability = probability
        self.probability_slide = probability_slide
        self.probability_slide_shape = probability_slide_shape
        self.prob_pos = prob_pos
        self.prob_pos_slide = prob_pos_slide
        self.prob_pos_slide_shape = prob_pos_slide_shape
        self.seed = seed
        self.smooth = smooth
        self.smooth_slide = smooth_slide
        self.smooth_slide_shape = smooth_slide_shape
        self.smooth_up = smooth_up
        self.smooth_up_slide = smooth_up_slide
        self.smooth_up_slide_shape = smooth_up_slide_shape
        self.smooth_down = smooth_down
        self.smooth_down_slide = smooth_down_slide
        self.smooth_down_slide_shape = smooth_down_slide_shape

    def get_ruby_effect_name(self) -> str:
        return "slicer"

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
            "phase": self.phase,
            "phase_slide": self.phase_slide,
            "phase_slide_shape": self.phase_slide_shape.value,
            "amp_min": self.amp_min,
            "amp_min_slide": self.amp_min_slide,
            "amp_min_slide_shape": self.amp_min_slide_shape.value,
            "amp_max": self.amp_max,
            "amp_max_slide": self.amp_max_slide,
            "amp_max_slide_shape": self.amp_max_slide_shape.value,
            "pulse_width": self.pulse_width,
            "pulse_width_slide": self.pulse_width_slide,
            "pulse_width_slide_shape": self.pulse_width_slide_shape.value,
            "phase_offset": self.phase_offset,
            "wave": self.wave,
            "invert_wave": self.invert_wave,
            "probability": self.probability,
            "probability_slide": self.probability_slide,
            "probability_slide_shape": self.probability_slide_shape.value,
            "prob_pos": self.prob_pos,
            "prob_pos_slide": self.prob_pos_slide,
            "prob_pos_slide_shape": self.prob_pos_slide_shape.value,
            "seed": self.seed,
            "smooth": self.smooth,
            "smooth_slide": self.smooth_slide,
            "smooth_slide_shape": self.smooth_slide_shape.value,
            "smooth_up": self.smooth_up,
            "smooth_up_slide": self.smooth_up_slide,
            "smooth_up_slide_shape": self.smooth_up_slide_shape.value,
            "smooth_down": self.smooth_down,
            "smooth_down_slide": self.smooth_down_slide,
            "smooth_down_slide_shape": self.smooth_down_slide_shape.value,
        }


class Wobble(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    phase: float = 0.5
    phase_slide: float = 0.0
    phase_slide_shape: SlideShape = SlideShape.LINEAR
    cutoff_min: float = 60.0
    cutoff_min_slide: float = 0.0
    cutoff_min_slide_shape: SlideShape = SlideShape.LINEAR
    cutoff_max: float = 120.0
    cutoff_max_slide: float = 0.0
    cutoff_max_slide_shape: SlideShape = SlideShape.LINEAR
    res: float = 0.8
    res_slide: float = 0.0
    res_slide_shape: SlideShape = SlideShape.LINEAR
    phase_offset: float = 0.0
    wave: float = 0.0
    invert_wave: float = 0.0
    pulse_width: float = 0.5
    pulse_width_slide: float = 0.0
    pulse_width_slide_shape: SlideShape = SlideShape.LINEAR
    filter: float = 0.0
    probability: float = 0.0
    probability_slide: float = 0.0
    probability_slide_shape: SlideShape = SlideShape.LINEAR
    prob_pos: float = 0.0
    prob_pos_slide: float = 0.0
    prob_pos_slide_shape: SlideShape = SlideShape.LINEAR
    seed: float = 0.0
    smooth: float = 0.0
    smooth_slide: float = 0.0
    smooth_slide_shape: SlideShape = SlideShape.LINEAR
    smooth_up: float = 0.0
    smooth_up_slide: float = 0.0
    smooth_up_slide_shape: SlideShape = SlideShape.LINEAR
    smooth_down: float = 0.0
    smooth_down_slide: float = 0.0
    smooth_down_slide_shape: SlideShape = SlideShape.LINEAR

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        phase: float = 0.5,
        phase_slide: float = 0.0,
        phase_slide_shape: SlideShape = SlideShape.LINEAR,
        cutoff_min: float = 60.0,
        cutoff_min_slide: float = 0.0,
        cutoff_min_slide_shape: SlideShape = SlideShape.LINEAR,
        cutoff_max: float = 120.0,
        cutoff_max_slide: float = 0.0,
        cutoff_max_slide_shape: SlideShape = SlideShape.LINEAR,
        res: float = 0.8,
        res_slide: float = 0.0,
        res_slide_shape: SlideShape = SlideShape.LINEAR,
        phase_offset: float = 0.0,
        wave: float = 0.0,
        invert_wave: float = 0.0,
        pulse_width: float = 0.5,
        pulse_width_slide: float = 0.0,
        pulse_width_slide_shape: SlideShape = SlideShape.LINEAR,
        filter: float = 0.0,
        probability: float = 0.0,
        probability_slide: float = 0.0,
        probability_slide_shape: SlideShape = SlideShape.LINEAR,
        prob_pos: float = 0.0,
        prob_pos_slide: float = 0.0,
        prob_pos_slide_shape: SlideShape = SlideShape.LINEAR,
        seed: float = 0.0,
        smooth: float = 0.0,
        smooth_slide: float = 0.0,
        smooth_slide_shape: SlideShape = SlideShape.LINEAR,
        smooth_up: float = 0.0,
        smooth_up_slide: float = 0.0,
        smooth_up_slide_shape: SlideShape = SlideShape.LINEAR,
        smooth_down: float = 0.0,
        smooth_down_slide: float = 0.0,
        smooth_down_slide_shape: SlideShape = SlideShape.LINEAR,
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
        self.phase = phase
        self.phase_slide = phase_slide
        self.phase_slide_shape = phase_slide_shape
        self.cutoff_min = cutoff_min
        self.cutoff_min_slide = cutoff_min_slide
        self.cutoff_min_slide_shape = cutoff_min_slide_shape
        self.cutoff_max = cutoff_max
        self.cutoff_max_slide = cutoff_max_slide
        self.cutoff_max_slide_shape = cutoff_max_slide_shape
        self.res = res
        self.res_slide = res_slide
        self.res_slide_shape = res_slide_shape
        self.phase_offset = phase_offset
        self.wave = wave
        self.invert_wave = invert_wave
        self.pulse_width = pulse_width
        self.pulse_width_slide = pulse_width_slide
        self.pulse_width_slide_shape = pulse_width_slide_shape
        self.filter = filter
        self.probability = probability
        self.probability_slide = probability_slide
        self.probability_slide_shape = probability_slide_shape
        self.prob_pos = prob_pos
        self.prob_pos_slide = prob_pos_slide
        self.prob_pos_slide_shape = prob_pos_slide_shape
        self.seed = seed
        self.smooth = smooth
        self.smooth_slide = smooth_slide
        self.smooth_slide_shape = smooth_slide_shape
        self.smooth_up = smooth_up
        self.smooth_up_slide = smooth_up_slide
        self.smooth_up_slide_shape = smooth_up_slide_shape
        self.smooth_down = smooth_down
        self.smooth_down_slide = smooth_down_slide
        self.smooth_down_slide_shape = smooth_down_slide_shape

    def get_ruby_effect_name(self) -> str:
        return "wobble"

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
            "phase": self.phase,
            "phase_slide": self.phase_slide,
            "phase_slide_shape": self.phase_slide_shape.value,
            "cutoff_min": self.cutoff_min,
            "cutoff_min_slide": self.cutoff_min_slide,
            "cutoff_min_slide_shape": self.cutoff_min_slide_shape.value,
            "cutoff_max": self.cutoff_max,
            "cutoff_max_slide": self.cutoff_max_slide,
            "cutoff_max_slide_shape": self.cutoff_max_slide_shape.value,
            "res": self.res,
            "res_slide": self.res_slide,
            "res_slide_shape": self.res_slide_shape.value,
            "phase_offset": self.phase_offset,
            "wave": self.wave,
            "invert_wave": self.invert_wave,
            "pulse_width": self.pulse_width,
            "pulse_width_slide": self.pulse_width_slide,
            "pulse_width_slide_shape": self.pulse_width_slide_shape.value,
            "filter": self.filter,
            "probability": self.probability,
            "probability_slide": self.probability_slide,
            "probability_slide_shape": self.probability_slide_shape.value,
            "prob_pos": self.prob_pos,
            "prob_pos_slide": self.prob_pos_slide,
            "prob_pos_slide_shape": self.prob_pos_slide_shape.value,
            "seed": self.seed,
            "smooth": self.smooth,
            "smooth_slide": self.smooth_slide,
            "smooth_slide_shape": self.smooth_slide_shape.value,
            "smooth_up": self.smooth_up,
            "smooth_up_slide": self.smooth_up_slide,
            "smooth_up_slide_shape": self.smooth_up_slide_shape.value,
            "smooth_down": self.smooth_down,
            "smooth_down_slide": self.smooth_down_slide,
            "smooth_down_slide_shape": self.smooth_down_slide_shape.value,
        }


class PanSlicer(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    phase: float = 0.25
    phase_slide: float = 0.0
    phase_slide_shape: SlideShape = SlideShape.LINEAR
    pan_min: float = -1.0
    pan_min_slide: float = 0.0
    pan_min_slide_shape: SlideShape = SlideShape.LINEAR
    pan_max: float = 1.0
    pan_max_slide: float = 0.0
    pan_max_slide_shape: SlideShape = SlideShape.LINEAR
    pulse_width: float = 0.5
    pulse_width_slide: float = 0.0
    pulse_width_slide_shape: SlideShape = SlideShape.LINEAR
    phase_offset: float = 0.0
    wave: float = 1.0
    invert_wave: float = 0.0
    probability: float = 0.0
    probability_slide: float = 0.0
    probability_slide_shape: SlideShape = SlideShape.LINEAR
    prob_pos: float = 0.0
    prob_pos_slide: float = 0.0
    prob_pos_slide_shape: SlideShape = SlideShape.LINEAR
    seed: float = 0.0
    smooth: float = 0.0
    smooth_slide: float = 0.0
    smooth_slide_shape: SlideShape = SlideShape.LINEAR
    smooth_up: float = 0.0
    smooth_up_slide: float = 0.0
    smooth_up_slide_shape: SlideShape = SlideShape.LINEAR
    smooth_down: float = 0.0
    smooth_down_slide: float = 0.0
    smooth_down_slide_shape: SlideShape = SlideShape.LINEAR

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        phase: float = 0.25,
        phase_slide: float = 0.0,
        phase_slide_shape: SlideShape = SlideShape.LINEAR,
        pan_min: float = -1.0,
        pan_min_slide: float = 0.0,
        pan_min_slide_shape: SlideShape = SlideShape.LINEAR,
        pan_max: float = 1.0,
        pan_max_slide: float = 0.0,
        pan_max_slide_shape: SlideShape = SlideShape.LINEAR,
        pulse_width: float = 0.5,
        pulse_width_slide: float = 0.0,
        pulse_width_slide_shape: SlideShape = SlideShape.LINEAR,
        phase_offset: float = 0.0,
        wave: float = 1.0,
        invert_wave: float = 0.0,
        probability: float = 0.0,
        probability_slide: float = 0.0,
        probability_slide_shape: SlideShape = SlideShape.LINEAR,
        prob_pos: float = 0.0,
        prob_pos_slide: float = 0.0,
        prob_pos_slide_shape: SlideShape = SlideShape.LINEAR,
        seed: float = 0.0,
        smooth: float = 0.0,
        smooth_slide: float = 0.0,
        smooth_slide_shape: SlideShape = SlideShape.LINEAR,
        smooth_up: float = 0.0,
        smooth_up_slide: float = 0.0,
        smooth_up_slide_shape: SlideShape = SlideShape.LINEAR,
        smooth_down: float = 0.0,
        smooth_down_slide: float = 0.0,
        smooth_down_slide_shape: SlideShape = SlideShape.LINEAR,
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
        self.phase = phase
        self.phase_slide = phase_slide
        self.phase_slide_shape = phase_slide_shape
        self.pan_min = pan_min
        self.pan_min_slide = pan_min_slide
        self.pan_min_slide_shape = pan_min_slide_shape
        self.pan_max = pan_max
        self.pan_max_slide = pan_max_slide
        self.pan_max_slide_shape = pan_max_slide_shape
        self.pulse_width = pulse_width
        self.pulse_width_slide = pulse_width_slide
        self.pulse_width_slide_shape = pulse_width_slide_shape
        self.phase_offset = phase_offset
        self.wave = wave
        self.invert_wave = invert_wave
        self.probability = probability
        self.probability_slide = probability_slide
        self.probability_slide_shape = probability_slide_shape
        self.prob_pos = prob_pos
        self.prob_pos_slide = prob_pos_slide
        self.prob_pos_slide_shape = prob_pos_slide_shape
        self.seed = seed
        self.smooth = smooth
        self.smooth_slide = smooth_slide
        self.smooth_slide_shape = smooth_slide_shape
        self.smooth_up = smooth_up
        self.smooth_up_slide = smooth_up_slide
        self.smooth_up_slide_shape = smooth_up_slide_shape
        self.smooth_down = smooth_down
        self.smooth_down_slide = smooth_down_slide
        self.smooth_down_slide_shape = smooth_down_slide_shape

    def get_ruby_effect_name(self) -> str:
        return "panslicer"

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
            "phase": self.phase,
            "phase_slide": self.phase_slide,
            "phase_slide_shape": self.phase_slide_shape.value,
            "pan_min": self.pan_min,
            "pan_min_slide": self.pan_min_slide,
            "pan_min_slide_shape": self.pan_min_slide_shape.value,
            "pan_max": self.pan_max,
            "pan_max_slide": self.pan_max_slide,
            "pan_max_slide_shape": self.pan_max_slide_shape.value,
            "pulse_width": self.pulse_width,
            "pulse_width_slide": self.pulse_width_slide,
            "pulse_width_slide_shape": self.pulse_width_slide_shape.value,
            "phase_offset": self.phase_offset,
            "wave": self.wave,
            "invert_wave": self.invert_wave,
            "probability": self.probability,
            "probability_slide": self.probability_slide,
            "probability_slide_shape": self.probability_slide_shape.value,
            "prob_pos": self.prob_pos,
            "prob_pos_slide": self.prob_pos_slide,
            "prob_pos_slide_shape": self.prob_pos_slide_shape.value,
            "seed": self.seed,
            "smooth": self.smooth,
            "smooth_slide": self.smooth_slide,
            "smooth_slide_shape": self.smooth_slide_shape.value,
            "smooth_up": self.smooth_up,
            "smooth_up_slide": self.smooth_up_slide,
            "smooth_up_slide_shape": self.smooth_up_slide_shape.value,
            "smooth_down": self.smooth_down,
            "smooth_down_slide": self.smooth_down_slide,
            "smooth_down_slide_shape": self.smooth_down_slide_shape.value,
        }


class IXITechno(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    phase: float = 4.0
    phase_slide: float = 0.0
    phase_slide_shape: SlideShape = SlideShape.LINEAR
    phase_offset: float = 0.0
    cutoff_min: float = 60.0
    cutoff_min_slide: float = 0.0
    cutoff_min_slide_shape: SlideShape = SlideShape.LINEAR
    cutoff_max: float = 120.0
    cutoff_max_slide: float = 0.0
    cutoff_max_slide_shape: SlideShape = SlideShape.LINEAR
    res: float = 0.8
    res_slide: float = 0.0
    res_slide_shape: SlideShape = SlideShape.LINEAR

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        phase: float = 4.0,
        phase_slide: float = 0.0,
        phase_slide_shape: SlideShape = SlideShape.LINEAR,
        phase_offset: float = 0.0,
        cutoff_min: float = 60.0,
        cutoff_min_slide: float = 0.0,
        cutoff_min_slide_shape: SlideShape = SlideShape.LINEAR,
        cutoff_max: float = 120.0,
        cutoff_max_slide: float = 0.0,
        cutoff_max_slide_shape: SlideShape = SlideShape.LINEAR,
        res: float = 0.8,
        res_slide: float = 0.0,
        res_slide_shape: SlideShape = SlideShape.LINEAR,
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
        self.phase = phase
        self.phase_slide = phase_slide
        self.phase_slide_shape = phase_slide_shape
        self.phase_offset = phase_offset
        self.cutoff_min = cutoff_min
        self.cutoff_min_slide = cutoff_min_slide
        self.cutoff_min_slide_shape = cutoff_min_slide_shape
        self.cutoff_max = cutoff_max
        self.cutoff_max_slide = cutoff_max_slide
        self.cutoff_max_slide_shape = cutoff_max_slide_shape
        self.res = res
        self.res_slide = res_slide
        self.res_slide_shape = res_slide_shape

    def get_ruby_effect_name(self) -> str:
        return "ixi_techno"

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
            "phase": self.phase,
            "phase_slide": self.phase_slide,
            "phase_slide_shape": self.phase_slide_shape.value,
            "phase_offset": self.phase_offset,
            "cutoff_min": self.cutoff_min,
            "cutoff_min_slide": self.cutoff_min_slide,
            "cutoff_min_slide_shape": self.cutoff_min_slide_shape.value,
            "cutoff_max": self.cutoff_max,
            "cutoff_max_slide": self.cutoff_max_slide,
            "cutoff_max_slide_shape": self.cutoff_max_slide_shape.value,
            "res": self.res,
            "res_slide": self.res_slide,
            "res_slide_shape": self.res_slide_shape.value,
        }


class Whammy(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    transpose: float = 12.0
    transpose_slide: float = 0.0
    transpose_slide_shape: SlideShape = SlideShape.LINEAR
    max_delay_time: float = 1.0
    deltime: float = 0.05
    grainsize: float = 0.075

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        transpose: float = 12.0,
        transpose_slide: float = 0.0,
        transpose_slide_shape: SlideShape = SlideShape.LINEAR,
        max_delay_time: float = 1.0,
        deltime: float = 0.05,
        grainsize: float = 0.075,
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
        self.transpose = transpose
        self.transpose_slide = transpose_slide
        self.transpose_slide_shape = transpose_slide_shape
        self.max_delay_time = max_delay_time
        self.deltime = deltime
        self.grainsize = grainsize

    def get_ruby_effect_name(self) -> str:
        return "whammy"

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
            "transpose": self.transpose,
            "transpose_slide": self.transpose_slide,
            "transpose_slide_shape": self.transpose_slide_shape.value,
            "max_delay_time": self.max_delay_time,
            "deltime": self.deltime,
            "grainsize": self.grainsize,
        }


class Compressor(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    threshold: float = 0.2
    threshold_slide: float = 0.0
    threshold_slide_shape: SlideShape = SlideShape.LINEAR
    ratio: float = 2.0
    ratio_slide: float = 0.0
    ratio_slide_shape: SlideShape = SlideShape.LINEAR
    attack: float = 0.01
    attack_slide: float = 0.0
    attack_slide_shape: SlideShape = SlideShape.LINEAR
    release: float = 0.1
    release_slide: float = 0.0
    release_slide_shape: SlideShape = SlideShape.LINEAR

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        threshold: float = 0.2,
        threshold_slide: float = 0.0,
        threshold_slide_shape: SlideShape = SlideShape.LINEAR,
        ratio: float = 2.0,
        ratio_slide: float = 0.0,
        ratio_slide_shape: SlideShape = SlideShape.LINEAR,
        attack: float = 0.01,
        attack_slide: float = 0.0,
        attack_slide_shape: SlideShape = SlideShape.LINEAR,
        release: float = 0.1,
        release_slide: float = 0.0,
        release_slide_shape: SlideShape = SlideShape.LINEAR,
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
        self.threshold = threshold
        self.threshold_slide = threshold_slide
        self.threshold_slide_shape = threshold_slide_shape
        self.ratio = ratio
        self.ratio_slide = ratio_slide
        self.ratio_slide_shape = ratio_slide_shape
        self.attack = attack
        self.attack_slide = attack_slide
        self.attack_slide_shape = attack_slide_shape
        self.release = release
        self.release_slide = release_slide
        self.release_slide_shape = release_slide_shape

    def get_ruby_effect_name(self) -> str:
        return "compressor"

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
            "threshold": self.threshold,
            "threshold_slide": self.threshold_slide,
            "threshold_slide_shape": self.threshold_slide_shape.value,
            "ratio": self.ratio,
            "ratio_slide": self.ratio_slide,
            "ratio_slide_shape": self.ratio_slide_shape.value,
            "attack": self.attack,
            "attack_slide": self.attack_slide,
            "attack_slide_shape": self.attack_slide_shape.value,
            "release": self.release,
            "release_slide": self.release_slide,
            "release_slide_shape": self.release_slide_shape.value,
        }


class Vowel(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    vowel: int = 0
    voice: int = 0

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        vowel: int = 0,
        voice: int = 0,
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
        self.vowel = vowel
        self.voice = voice

    def get_ruby_effect_name(self) -> str:
        return "vowel"

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
            "vowel": self.vowel,
            "voice": self.voice,
        }


class Octaver(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    super_amp: float = 1.0
    super_amp_slide: float = 0.0
    super_amp_slide_shape: SlideShape = SlideShape.LINEAR
    sub_amp: float = 1.0
    sub_amp_slide: float = 0.0
    sub_amp_slide_shape: SlideShape = SlideShape.LINEAR
    subsub_amp: float = 1.0
    subsub_amp_slide: float = 0.0
    subsub_amp_slide_shape: SlideShape = SlideShape.LINEAR

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        super_amp: float = 1.0,
        super_amp_slide: float = 0.0,
        super_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        sub_amp: float = 1.0,
        sub_amp_slide: float = 0.0,
        sub_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        subsub_amp: float = 1.0,
        subsub_amp_slide: float = 0.0,
        subsub_amp_slide_shape: SlideShape = SlideShape.LINEAR,
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
        self.super_amp = super_amp
        self.super_amp_slide = super_amp_slide
        self.super_amp_slide_shape = super_amp_slide_shape
        self.sub_amp = sub_amp
        self.sub_amp_slide = sub_amp_slide
        self.sub_amp_slide_shape = sub_amp_slide_shape
        self.subsub_amp = subsub_amp
        self.subsub_amp_slide = subsub_amp_slide
        self.subsub_amp_slide_shape = subsub_amp_slide_shape

    def get_ruby_effect_name(self) -> str:
        return "octaver"

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
            "super_amp": self.super_amp,
            "super_amp_slide": self.super_amp_slide,
            "super_amp_slide_shape": self.super_amp_slide_shape.value,
            "sub_amp": self.sub_amp,
            "sub_amp_slide": self.sub_amp_slide,
            "sub_amp_slide_shape": self.sub_amp_slide_shape.value,
            "subsub_amp": self.subsub_amp,
            "subsub_amp_slide": self.subsub_amp_slide,
            "subsub_amp_slide_shape": self.subsub_amp_slide_shape.value,
        }


class Chorus(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    phase: float = 0.25
    phase_slide: float = 0.0
    phase_slide_shape: SlideShape = SlideShape.LINEAR
    decay: float = 0.0
    decay_slide: float = 0.0
    decay_slide_shape: SlideShape = SlideShape.LINEAR
    max_phase: float = 1.0

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        phase: float = 0.25,
        phase_slide: float = 0.0,
        phase_slide_shape: SlideShape = SlideShape.LINEAR,
        decay: float = 0.0,
        decay_slide: float = 0.0,
        decay_slide_shape: SlideShape = SlideShape.LINEAR,
        max_phase: float = 1.0,
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
        self.phase = phase
        self.phase_slide = phase_slide
        self.phase_slide_shape = phase_slide_shape
        self.decay = decay
        self.decay_slide = decay_slide
        self.decay_slide_shape = decay_slide_shape
        self.max_phase = max_phase

    def get_ruby_effect_name(self) -> str:
        return "chorus"

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
            "phase": self.phase,
            "phase_slide": self.phase_slide,
            "phase_slide_shape": self.phase_slide_shape.value,
            "decay": self.decay,
            "decay_slide": self.decay_slide,
            "decay_slide_shape": self.decay_slide_shape.value,
            "max_phase": self.max_phase,
        }


class RingMod(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    freq: float = 30.0
    freq_slide: float = 0.0
    freq_slide_shape: SlideShape = SlideShape.LINEAR
    mod_amp: float = 1.0
    mod_amp_slide: float = 0.0
    mod_amp_slide_shape: SlideShape = SlideShape.LINEAR

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        freq: float = 30.0,
        freq_slide: float = 0.0,
        freq_slide_shape: SlideShape = SlideShape.LINEAR,
        mod_amp: float = 1.0,
        mod_amp_slide: float = 0.0,
        mod_amp_slide_shape: SlideShape = SlideShape.LINEAR,
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
        self.freq = freq
        self.freq_slide = freq_slide
        self.freq_slide_shape = freq_slide_shape
        self.mod_amp = mod_amp
        self.mod_amp_slide = mod_amp_slide
        self.mod_amp_slide_shape = mod_amp_slide_shape

    def get_ruby_effect_name(self) -> str:
        return "ring_mod"

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
            "freq": self.freq,
            "freq_slide": self.freq_slide,
            "freq_slide_shape": self.freq_slide_shape.value,
            "mod_amp": self.mod_amp,
            "mod_amp_slide": self.mod_amp_slide,
            "mod_amp_slide_shape": self.mod_amp_slide_shape.value,
        }


class BPF(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    cutoff: float = 100.0
    cutoff_slide: float = 0.0
    cutoff_slide_shape: SlideShape = SlideShape.LINEAR

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        cutoff: float = 100.0,
        cutoff_slide: float = 0.0,
        cutoff_slide_shape: SlideShape = SlideShape.LINEAR,
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
        self.cutoff = cutoff
        self.cutoff_slide = cutoff_slide
        self.cutoff_slide_shape = cutoff_slide_shape

    def get_ruby_effect_name(self) -> str:
        return "bpf"

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
            "cutoff": self.cutoff,
            "cutoff_slide": self.cutoff_slide,
            "cutoff_slide_shape": self.cutoff_slide_shape.value,
        }


class RBPF(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    cutoff: float = 100.0
    cutoff_slide: float = 0.0
    cutoff_slide_shape: SlideShape = SlideShape.LINEAR
    res: float = 0.5
    res_slide: float = 0.0
    res_slide_shape: SlideShape = SlideShape.LINEAR

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        cutoff: float = 100.0,
        cutoff_slide: float = 0.0,
        cutoff_slide_shape: SlideShape = SlideShape.LINEAR,
        res: float = 0.5,
        res_slide: float = 0.0,
        res_slide_shape: SlideShape = SlideShape.LINEAR,
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
        self.cutoff = cutoff
        self.cutoff_slide = cutoff_slide
        self.cutoff_slide_shape = cutoff_slide_shape
        self.res = res
        self.res_slide = res_slide
        self.res_slide_shape = res_slide_shape

    def get_ruby_effect_name(self) -> str:
        return "rbpf"

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
            "cutoff": self.cutoff,
            "cutoff_slide": self.cutoff_slide,
            "cutoff_slide_shape": self.cutoff_slide_shape.value,
            "res": self.res,
            "res_slide": self.res_slide,
            "res_slide_shape": self.res_slide_shape.value,
        }


class NBPF(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    cutoff: float = 100.0
    cutoff_slide: float = 0.0
    cutoff_slide_shape: SlideShape = SlideShape.LINEAR

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        cutoff: float = 100.0,
        cutoff_slide: float = 0.0,
        cutoff_slide_shape: SlideShape = SlideShape.LINEAR,
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
        self.cutoff = cutoff
        self.cutoff_slide = cutoff_slide
        self.cutoff_slide_shape = cutoff_slide_shape

    def get_ruby_effect_name(self) -> str:
        return "nbpf"

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
            "cutoff": self.cutoff,
            "cutoff_slide": self.cutoff_slide,
            "cutoff_slide_shape": self.cutoff_slide_shape.value,
        }


class NRBPF(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    cutoff: float = 100.0
    cutoff_slide: float = 0.0
    cutoff_slide_shape: SlideShape = SlideShape.LINEAR
    res: float = 0.5
    res_slide: float = 0.0
    res_slide_shape: SlideShape = SlideShape.LINEAR

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        cutoff: float = 100.0,
        cutoff_slide: float = 0.0,
        cutoff_slide_shape: SlideShape = SlideShape.LINEAR,
        res: float = 0.5,
        res_slide: float = 0.0,
        res_slide_shape: SlideShape = SlideShape.LINEAR,
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
        self.cutoff = cutoff
        self.cutoff_slide = cutoff_slide
        self.cutoff_slide_shape = cutoff_slide_shape
        self.res = res
        self.res_slide = res_slide
        self.res_slide_shape = res_slide_shape

    def get_ruby_effect_name(self) -> str:
        return "nrbpf"

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
            "cutoff": self.cutoff,
            "cutoff_slide": self.cutoff_slide,
            "cutoff_slide_shape": self.cutoff_slide_shape.value,
            "res": self.res,
            "res_slide": self.res_slide,
            "res_slide_shape": self.res_slide_shape.value,
        }


class LPF(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    cutoff: float = 100.0
    cutoff_slide: float = 0.0
    cutoff_slide_shape: SlideShape = SlideShape.LINEAR

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        cutoff: float = 100.0,
        cutoff_slide: float = 0.0,
        cutoff_slide_shape: SlideShape = SlideShape.LINEAR,
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
        self.cutoff = cutoff
        self.cutoff_slide = cutoff_slide
        self.cutoff_slide_shape = cutoff_slide_shape

    def get_ruby_effect_name(self) -> str:
        return "lpf"

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
            "cutoff": self.cutoff,
            "cutoff_slide": self.cutoff_slide,
            "cutoff_slide_shape": self.cutoff_slide_shape.value,
        }


class RLPF(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    cutoff: float = 100.0
    cutoff_slide: float = 0.0
    cutoff_slide_shape: SlideShape = SlideShape.LINEAR
    res: float = 0.5
    res_slide: float = 0.0
    res_slide_shape: SlideShape = SlideShape.LINEAR

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        cutoff: float = 100.0,
        cutoff_slide: float = 0.0,
        cutoff_slide_shape: SlideShape = SlideShape.LINEAR,
        res: float = 0.5,
        res_slide: float = 0.0,
        res_slide_shape: SlideShape = SlideShape.LINEAR,
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
        self.cutoff = cutoff
        self.cutoff_slide = cutoff_slide
        self.cutoff_slide_shape = cutoff_slide_shape
        self.res = res
        self.res_slide = res_slide
        self.res_slide_shape = res_slide_shape

    def get_ruby_effect_name(self) -> str:
        return "rlpf"

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
            "cutoff": self.cutoff,
            "cutoff_slide": self.cutoff_slide,
            "cutoff_slide_shape": self.cutoff_slide_shape.value,
            "res": self.res,
            "res_slide": self.res_slide,
            "res_slide_shape": self.res_slide_shape.value,
        }


class NormRLPF(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    cutoff: float = 100.0
    cutoff_slide: float = 0.0
    cutoff_slide_shape: SlideShape = SlideShape.LINEAR
    res: float = 0.5
    res_slide: float = 0.0
    res_slide_shape: SlideShape = SlideShape.LINEAR

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        cutoff: float = 100.0,
        cutoff_slide: float = 0.0,
        cutoff_slide_shape: SlideShape = SlideShape.LINEAR,
        res: float = 0.5,
        res_slide: float = 0.0,
        res_slide_shape: SlideShape = SlideShape.LINEAR,
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
        self.cutoff = cutoff
        self.cutoff_slide = cutoff_slide
        self.cutoff_slide_shape = cutoff_slide_shape
        self.res = res
        self.res_slide = res_slide
        self.res_slide_shape = res_slide_shape

    def get_ruby_effect_name(self) -> str:
        return "norm_rlpf"

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
            "cutoff": self.cutoff,
            "cutoff_slide": self.cutoff_slide,
            "cutoff_slide_shape": self.cutoff_slide_shape.value,
            "res": self.res,
            "res_slide": self.res_slide,
            "res_slide_shape": self.res_slide_shape.value,
        }


class HPF(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    cutoff: float = 100.0
    cutoff_slide: float = 0.0
    cutoff_slide_shape: SlideShape = SlideShape.LINEAR

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        cutoff: float = 100.0,
        cutoff_slide: float = 0.0,
        cutoff_slide_shape: SlideShape = SlideShape.LINEAR,
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
        self.cutoff = cutoff
        self.cutoff_slide = cutoff_slide
        self.cutoff_slide_shape = cutoff_slide_shape

    def get_ruby_effect_name(self) -> str:
        return "hpf"

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
            "cutoff": self.cutoff,
            "cutoff_slide": self.cutoff_slide,
            "cutoff_slide_shape": self.cutoff_slide_shape.value,
        }


class RHPF(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    cutoff: float = 100.0
    cutoff_slide: float = 0.0
    cutoff_slide_shape: SlideShape = SlideShape.LINEAR
    res: float = 0.5
    res_slide: float = 0.0
    res_slide_shape: SlideShape = SlideShape.LINEAR

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        cutoff: float = 100.0,
        cutoff_slide: float = 0.0,
        cutoff_slide_shape: SlideShape = SlideShape.LINEAR,
        res: float = 0.5,
        res_slide: float = 0.0,
        res_slide_shape: SlideShape = SlideShape.LINEAR,
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
        self.cutoff = cutoff
        self.cutoff_slide = cutoff_slide
        self.cutoff_slide_shape = cutoff_slide_shape
        self.res = res
        self.res_slide = res_slide
        self.res_slide_shape = res_slide_shape

    def get_ruby_effect_name(self) -> str:
        return "rhpf"

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
            "cutoff": self.cutoff,
            "cutoff_slide": self.cutoff_slide,
            "cutoff_slide_shape": self.cutoff_slide_shape.value,
            "res": self.res,
            "res_slide": self.res_slide,
            "res_slide_shape": self.res_slide_shape.value,
        }


class NormRHPF(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    cutoff: float = 100.0
    cutoff_slide: float = 0.0
    cutoff_slide_shape: SlideShape = SlideShape.LINEAR
    res: float = 0.5
    res_slide: float = 0.0
    res_slide_shape: SlideShape = SlideShape.LINEAR

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        cutoff: float = 100.0,
        cutoff_slide: float = 0.0,
        cutoff_slide_shape: SlideShape = SlideShape.LINEAR,
        res: float = 0.5,
        res_slide: float = 0.0,
        res_slide_shape: SlideShape = SlideShape.LINEAR,
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
        self.cutoff = cutoff
        self.cutoff_slide = cutoff_slide
        self.cutoff_slide_shape = cutoff_slide_shape
        self.res = res
        self.res_slide = res_slide
        self.res_slide_shape = res_slide_shape

    def get_ruby_effect_name(self) -> str:
        return "norm_rhpf"

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
            "cutoff": self.cutoff,
            "cutoff_slide": self.cutoff_slide,
            "cutoff_slide_shape": self.cutoff_slide_shape.value,
            "res": self.res,
            "res_slide": self.res_slide,
            "res_slide_shape": self.res_slide_shape.value,
        }


class BandEQ(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    low: float = 0.0
    low_slide: float = 0.0
    low_slide_shape: SlideShape = SlideShape.LINEAR
    low_freq: float = 100.0
    low_freq_slide: float = 0.0
    low_freq_slide_shape: SlideShape = SlideShape.LINEAR
    mid: float = 0.0
    mid_slide: float = 0.0
    mid_slide_shape: SlideShape = SlideShape.LINEAR
    mid_freq: float = 1000.0
    mid_freq_slide: float = 0.0
    mid_freq_slide_shape: SlideShape = SlideShape.LINEAR
    high: float = 0.0
    high_slide: float = 0.0
    high_slide_shape: SlideShape = SlideShape.LINEAR
    high_freq: float = 10000.0
    high_freq_slide: float = 0.0
    high_freq_slide_shape: SlideShape = SlideShape.LINEAR

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        low: float = 0.0,
        low_slide: float = 0.0,
        low_slide_shape: SlideShape = SlideShape.LINEAR,
        low_freq: float = 100.0,
        low_freq_slide: float = 0.0,
        low_freq_slide_shape: SlideShape = SlideShape.LINEAR,
        mid: float = 0.0,
        mid_slide: float = 0.0,
        mid_slide_shape: SlideShape = SlideShape.LINEAR,
        mid_freq: float = 1000.0,
        mid_freq_slide: float = 0.0,
        mid_freq_slide_shape: SlideShape = SlideShape.LINEAR,
        high: float = 0.0,
        high_slide: float = 0.0,
        high_slide_shape: SlideShape = SlideShape.LINEAR,
        high_freq: float = 10000.0,
        high_freq_slide: float = 0.0,
        high_freq_slide_shape: SlideShape = SlideShape.LINEAR,
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
        self.low = low
        self.low_slide = low_slide
        self.low_slide_shape = low_slide_shape
        self.low_freq = low_freq
        self.low_freq_slide = low_freq_slide
        self.low_freq_slide_shape = low_freq_slide_shape
        self.mid = mid
        self.mid_slide = mid_slide
        self.mid_slide_shape = mid_slide_shape
        self.mid_freq = mid_freq
        self.mid_freq_slide = mid_freq_slide
        self.mid_freq_slide_shape = mid_freq_slide_shape
        self.high = high
        self.high_slide = high_slide
        self.high_slide_shape = high_slide_shape
        self.high_freq = high_freq
        self.high_freq_slide = high_freq_slide
        self.high_freq_slide_shape = high_freq_slide_shape

    def get_ruby_effect_name(self) -> str:
        return "band_eq"

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
            "low": self.low,
            "low_slide": self.low_slide,
            "low_slide_shape": self.low_slide_shape.value,
            "low_freq": self.low_freq,
            "low_freq_slide": self.low_freq_slide,
            "low_freq_slide_shape": self.low_freq_slide_shape.value,
            "mid": self.mid,
            "mid_slide": self.mid_slide,
            "mid_slide_shape": self.mid_slide_shape.value,
            "mid_freq": self.mid_freq,
            "mid_freq_slide": self.mid_freq_slide,
            "mid_freq_slide_shape": self.mid_freq_slide_shape.value,
            "high": self.high,
            "high_slide": self.high_slide,
            "high_slide_shape": self.high_slide_shape.value,
            "high_freq": self.high_freq,
            "high_freq_slide": self.high_freq_slide,
            "high_freq_slide_shape": self.high_freq_slide_shape.value,
        }


class NormLPF(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    cutoff: float = 100.0
    cutoff_slide: float = 0.0
    cutoff_slide_shape: SlideShape = SlideShape.LINEAR

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        cutoff: float = 100.0,
        cutoff_slide: float = 0.0,
        cutoff_slide_shape: SlideShape = SlideShape.LINEAR,
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
        self.cutoff = cutoff
        self.cutoff_slide = cutoff_slide
        self.cutoff_slide_shape = cutoff_slide_shape

    def get_ruby_effect_name(self) -> str:
        return "norm_lpf"

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
            "cutoff": self.cutoff,
            "cutoff_slide": self.cutoff_slide,
            "cutoff_slide_shape": self.cutoff_slide_shape.value,
        }


class NormHPF(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    cutoff: float = 100.0
    cutoff_slide: float = 0.0
    cutoff_slide_shape: SlideShape = SlideShape.LINEAR

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        cutoff: float = 100.0,
        cutoff_slide: float = 0.0,
        cutoff_slide_shape: SlideShape = SlideShape.LINEAR,
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
        self.cutoff = cutoff
        self.cutoff_slide = cutoff_slide
        self.cutoff_slide_shape = cutoff_slide_shape

    def get_ruby_effect_name(self) -> str:
        return "norm_hpf"

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
            "cutoff": self.cutoff,
            "cutoff_slide": self.cutoff_slide,
            "cutoff_slide_shape": self.cutoff_slide_shape.value,
        }


class Normaliser(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
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

    def get_ruby_effect_name(self) -> str:
        return "normaliser"

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
        }


class Tanh(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    krunch: float = 2.0
    krunch_slide: float = 0.0
    krunch_slide_shape: SlideShape = SlideShape.LINEAR

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        krunch: float = 2.0,
        krunch_slide: float = 0.0,
        krunch_slide_shape: SlideShape = SlideShape.LINEAR,
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
        self.krunch = krunch
        self.krunch_slide = krunch_slide
        self.krunch_slide_shape = krunch_slide_shape

    def get_ruby_effect_name(self) -> str:
        return "tanh"

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
            "krunch": self.krunch,
            "krunch_slide": self.krunch_slide,
            "krunch_slide_shape": self.krunch_slide_shape.value,
        }


class PitchShift(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    transpose: float = 0.0
    transpose_slide: float = 0.0
    transpose_slide_shape: SlideShape = SlideShape.LINEAR
    window_size: float = 0.2
    window_size_slide: float = 0.0
    window_size_slide_shape: SlideShape = SlideShape.LINEAR
    pitch_dis: float = 0.0
    pitch_dis_slide: float = 0.0
    pitch_dis_slide_shape: SlideShape = SlideShape.LINEAR
    time_dis: float = 0.0
    time_dis_slide: float = 0.0
    time_dis_slide_shape: SlideShape = SlideShape.LINEAR

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        transpose: float = 0.0,
        transpose_slide: float = 0.0,
        transpose_slide_shape: SlideShape = SlideShape.LINEAR,
        window_size: float = 0.2,
        window_size_slide: float = 0.0,
        window_size_slide_shape: SlideShape = SlideShape.LINEAR,
        pitch_dis: float = 0.0,
        pitch_dis_slide: float = 0.0,
        pitch_dis_slide_shape: SlideShape = SlideShape.LINEAR,
        time_dis: float = 0.0,
        time_dis_slide: float = 0.0,
        time_dis_slide_shape: SlideShape = SlideShape.LINEAR,
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
        self.transpose = transpose
        self.transpose_slide = transpose_slide
        self.transpose_slide_shape = transpose_slide_shape
        self.window_size = window_size
        self.window_size_slide = window_size_slide
        self.window_size_slide_shape = window_size_slide_shape
        self.pitch_dis = pitch_dis
        self.pitch_dis_slide = pitch_dis_slide
        self.pitch_dis_slide_shape = pitch_dis_slide_shape
        self.time_dis = time_dis
        self.time_dis_slide = time_dis_slide
        self.time_dis_slide_shape = time_dis_slide_shape

    def get_ruby_effect_name(self) -> str:
        return "pitch_shift"

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
            "transpose": self.transpose,
            "transpose_slide": self.transpose_slide,
            "transpose_slide_shape": self.transpose_slide_shape.value,
            "window_size": self.window_size,
            "window_size_slide": self.window_size_slide,
            "window_size_slide_shape": self.window_size_slide_shape.value,
            "pitch_dis": self.pitch_dis,
            "pitch_dis_slide": self.pitch_dis_slide,
            "pitch_dis_slide_shape": self.pitch_dis_slide_shape.value,
            "time_dis": self.time_dis,
            "time_dis_slide": self.time_dis_slide,
            "time_dis_slide_shape": self.time_dis_slide_shape.value,
        }


class Distortion(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    distort: float = 0.5
    distort_slide: float = 0.0
    distort_slide_shape: SlideShape = SlideShape.LINEAR

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        distort: float = 0.5,
        distort_slide: float = 0.0,
        distort_slide_shape: SlideShape = SlideShape.LINEAR,
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
        self.distort = distort
        self.distort_slide = distort_slide
        self.distort_slide_shape = distort_slide_shape

    def get_ruby_effect_name(self) -> str:
        return "distortion"

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
            "distort": self.distort,
            "distort_slide": self.distort_slide,
            "distort_slide_shape": self.distort_slide_shape.value,
        }


class Flanger(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    phase: float = 4.0
    phase_slide: float = 0.0
    phase_slide_shape: SlideShape = SlideShape.LINEAR
    decay: float = 2.0
    decay_slide: float = 0.0
    decay_slide_shape: SlideShape = SlideShape.LINEAR
    max_phase: float = 2.0

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        phase: float = 4.0,
        phase_slide: float = 0.0,
        phase_slide_shape: SlideShape = SlideShape.LINEAR,
        decay: float = 2.0,
        decay_slide: float = 0.0,
        decay_slide_shape: SlideShape = SlideShape.LINEAR,
        max_phase: float = 2.0,
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
        self.phase = phase
        self.phase_slide = phase_slide
        self.phase_slide_shape = phase_slide_shape
        self.decay = decay
        self.decay_slide = decay_slide
        self.decay_slide_shape = decay_slide_shape
        self.max_phase = max_phase

    def get_ruby_effect_name(self) -> str:
        return "flanger"

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
            "phase": self.phase,
            "phase_slide": self.phase_slide,
            "phase_slide_shape": self.phase_slide_shape.value,
            "decay": self.decay,
            "decay_slide": self.decay_slide,
            "decay_slide_shape": self.decay_slide_shape.value,
            "max_phase": self.max_phase,
        }


class Tremolo(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    phase: float = 4.0
    phase_slide: float = 0.0
    phase_slide_shape: SlideShape = SlideShape.LINEAR
    amp_min: float = 0.0
    amp_min_slide: float = 0.0
    amp_min_slide_shape: SlideShape = SlideShape.LINEAR
    amp_max: float = 1.0
    amp_max_slide: float = 0.0
    amp_max_slide_shape: SlideShape = SlideShape.LINEAR

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        phase: float = 4.0,
        phase_slide: float = 0.0,
        phase_slide_shape: SlideShape = SlideShape.LINEAR,
        amp_min: float = 0.0,
        amp_min_slide: float = 0.0,
        amp_min_slide_shape: SlideShape = SlideShape.LINEAR,
        amp_max: float = 1.0,
        amp_max_slide: float = 0.0,
        amp_max_slide_shape: SlideShape = SlideShape.LINEAR,
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
        self.phase = phase
        self.phase_slide = phase_slide
        self.phase_slide_shape = phase_slide_shape
        self.amp_min = amp_min
        self.amp_min_slide = amp_min_slide
        self.amp_min_slide_shape = amp_min_slide_shape
        self.amp_max = amp_max
        self.amp_max_slide = amp_max_slide
        self.amp_max_slide_shape = amp_max_slide_shape

    def get_ruby_effect_name(self) -> str:
        return "tremolo"

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
            "phase": self.phase,
            "phase_slide": self.phase_slide,
            "phase_slide_shape": self.phase_slide_shape.value,
            "amp_min": self.amp_min,
            "amp_min_slide": self.amp_min_slide,
            "amp_min_slide_shape": self.amp_min_slide_shape.value,
            "amp_max": self.amp_max,
            "amp_max_slide": self.amp_max_slide,
            "amp_max_slide_shape": self.amp_max_slide_shape.value,
        }


class PingPong(EffectInstance):
    amp: float = 1.0
    amp_slide: float = 0.0
    amp_slide_shape: SlideShape = SlideShape.LINEAR
    mix: float = 1.0
    mix_slide: float = 0.0
    mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_mix: float = 1.0
    pre_mix_slide: float = 0.0
    pre_mix_slide_shape: SlideShape = SlideShape.LINEAR
    pre_amp: float = 1.0
    pre_amp_slide: float = 0.0
    pre_amp_slide_shape: SlideShape = SlideShape.LINEAR
    phase: float = 0.25
    phase_slide: float = 0.0
    phase_slide_shape: SlideShape = SlideShape.LINEAR
    decay: float = 2.0
    decay_slide: float = 0.0
    decay_slide_shape: SlideShape = SlideShape.LINEAR
    max_phase: float = 2.0

    def __init__(
        self,
        id: str,
        amp: float = 1.0,
        amp_slide: float = 0.0,
        amp_slide_shape: SlideShape = SlideShape.LINEAR,
        mix: float = 1.0,
        mix_slide: float = 0.0,
        mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_mix: float = 1.0,
        pre_mix_slide: float = 0.0,
        pre_mix_slide_shape: SlideShape = SlideShape.LINEAR,
        pre_amp: float = 1.0,
        pre_amp_slide: float = 0.0,
        pre_amp_slide_shape: SlideShape = SlideShape.LINEAR,
        phase: float = 0.25,
        phase_slide: float = 0.0,
        phase_slide_shape: SlideShape = SlideShape.LINEAR,
        decay: float = 2.0,
        decay_slide: float = 0.0,
        decay_slide_shape: SlideShape = SlideShape.LINEAR,
        max_phase: float = 2.0,
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
        self.phase = phase
        self.phase_slide = phase_slide
        self.phase_slide_shape = phase_slide_shape
        self.decay = decay
        self.decay_slide = decay_slide
        self.decay_slide_shape = decay_slide_shape
        self.max_phase = max_phase

    def get_ruby_effect_name(self) -> str:
        return "ping_pong"

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
            "phase": self.phase,
            "phase_slide": self.phase_slide,
            "phase_slide_shape": self.phase_slide_shape.value,
            "decay": self.decay,
            "decay_slide": self.decay_slide,
            "decay_slide_shape": self.decay_slide_shape.value,
            "max_phase": self.max_phase,
        }


ALL_EFFECT_CLASSES = EffectInstance.__subclasses__()


def get_effect_class_by_ruby_name(effect_ruby_name) -> type[EffectInstance]:
    for effect_class in ALL_EFFECT_CLASSES:
        if effect_class.get_ruby_effect_name(effect_class) == effect_ruby_name:
            return effect_class
    raise ValueError(f"Effect class with ruby name '{effect_ruby_name}' not found.")
