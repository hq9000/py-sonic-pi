from py_sonic_pi.effects import HPFilter, Reverb
from py_sonic_pi.inventory import (
    GroupTrack,
    GeneratorTrack,
    Pattern,
    Project,
    Sample,
    Sampler,
    Sleep,
    StockSampleName,
    Note,
    Pattern,
    Sync,
    Tb303,
)
from py_sonic_pi.patterns import construct_pattern_from_matter
from py_sonic_pi.transformer import transform

bass_pattern_elements = [
    Sync(n_bars=1),
    Sleep(0.5),
    Note(40),
    Sleep(1),
    Note(40),
    Sleep(1),
    Note(40),
    Sleep(0.75),
    Note(41),
]

bd_pattern = construct_pattern_from_matter(
    """
        sync: 1
        resolution: 0.25
        notes: 0____0____0____0
    """
)

bass_pattern = construct_pattern_from_matter(
    """
        sync: 1
        resolution: 0.5
        base_note: C3
        base_release: 0.1
        notes: _0__12__1__0_
    """
)

bd_track = GeneratorTrack(
    id="bd",
    generator=Sampler(Sample(stock_sample_name=StockSampleName.BD_HAUS)),
    pattern=bd_pattern,
)
crash_track = GeneratorTrack(
    id="crash",
    generator=Sampler(Sample(stock_sample_name=StockSampleName.RIDE_TRI)),
    gain=0.5,
    pattern=construct_pattern_from_matter(
        """
        sync: 1
        notes: 0
        """
    ),
)
bass_track = GeneratorTrack(
    id="bass",
    generator=Tb303(),
    pattern=bass_pattern,
    effects=[Reverb(id="bass_reverb")],
)
bass_bd = GroupTrack(
    id="bass_bd",
    children=[bd_track, bass_track],
    effects=[Reverb(id="bass_bd_reverb", room=1)],
)


bass_track.gain = 0.3
bass_track.pan = 0.5
bass_track.muted = False


master_track = GroupTrack(
    id="master",
    children=[bass_bd, crash_track],
    effects=[HPFilter(id="masterhpf", cutoff=0.0, controllable=True)],
)

p = Project(top_level_tracks=[master_track], beat_length_seconds=0.45)

lines = transform(p)
with open("output.rb", "w") as f:
    for line in lines:
        f.write(line + "\n")
