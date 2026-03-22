class Generator:
    pass

class Synth(Generator):
    pass

class Sample(Generator):
    pass

class Effect:
    pass

class Pattern:
    pass


class Track:
    def __init__(self, generator: Generator, pattern: Pattern, effects: list[Effect]):
        self.generator = generator
        self.pattern = pattern
        self.effects = effects
    pass


class Project:
    def __init__(self, tracks: list[Track]):
        self.tracks = tracks