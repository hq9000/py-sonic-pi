from dataclasses import dataclass
from enum import Enum


class Generator:
    pass

class Synth(Generator):
    pass

class SampleName(Enum):
    BD_HAUS = "bd_haus"


@dataclass
class Sample(Generator):
    name: SampleName|None = None

class Effect:
    pass

@dataclass
class HPFilter(Effect):
    cutoff: float = 0.0
    resonance: float = 0.0

@dataclass
class Pattern:
    raw: str

class Track:
    def __init__(self, generator: Generator, pattern: Pattern, effects: list[Effect] = []):
        self.generator = generator
        self.pattern = pattern
        self.effects = effects
    pass


class Project:
    def __init__(self, tracks: list[Track], master_effects: list[Effect] = []):
        self.tracks = tracks
        self.master_effects = master_effects

