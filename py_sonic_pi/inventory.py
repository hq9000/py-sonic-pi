from dataclasses import dataclass, field
from enum import Enum
from abc import ABC

class Generator:
    pass

class Synth(Generator):
    pass

class StockSampleName(Enum):
    BD_HAUS = "bd_haus"

class Sample:
    def __init__(self, stock_sample_name: StockSampleName|None = None, sample_path: str|None = None):
        self.name = stock_sample_name
        self.sample_path = sample_path
        if self.name is None and self.sample_path is None:
            raise ValueError("Either stock_sample_name or sample_path must be provided")

@dataclass
class Sampler(Generator):
    sample: Sample|None = None


@dataclass
class Effect:
    id: str = ""

@dataclass
class HPFilter(Effect):
    cutoff: float = 0.0
    resonance: float = 0.0


class PatternElement(ABC):
    pass

@dataclass
class Note(PatternElement):
    note: float = 0.0
    amp: float = 1.0
    pan: float = 0.0
    attack_seconds: float = 0.0
    decay_seconds: float = 0.0
    sustain_seconds: float = 0.5
    release_seconds: float = 0.0
    sample: Sample|None = None
    rate: float = 1.0


class Sleep(PatternElement):
    def __init__(self, duration_beats: float):
        self.duration_beats = duration_beats


class Pattern(ABC):
    pass

@dataclass
class SamplePattern(Pattern):
    elements: list[PatternElement] = field(default_factory=list)
    every_n_bars: int = 1

class TrackType(Enum):
    SYNTH = "synth"
    SAMPLE = "sample"
@dataclass
class Track(ABC):
    id = id
    effects: list[Effect] = field(default_factory=list)
    gain: float = 1.0
    pan: float = 0.0
    mute: bool = False
    solo: bool = False

@dataclass
class GeneratorTrack(Track):
    generator: Generator
    pattern: Pattern

    def getTrackType(self) -> TrackType:
        return TrackType.SYNTH if isinstance(self.generator, Synth) else TrackType.SAMPLE


@dataclass
class BusTrack(Track):
    children: list[Track] = field(default_factory=list)


class Project:
    def __init__(self, tracks: list[Track], master_effects: list[Effect] = [], beat_length_seconds: float = 0.5):
        self.tracks = tracks
        self.master_effects = master_effects
        self.beat_length_seconds = beat_length_seconds

