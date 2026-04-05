from py_sonic_pi.effects import HPFilter, Reverb
from py_sonic_pi.inventory import GroupTrack, GeneratorTrack, Pattern, Project, Sample, Sampler, Sleep, StockSampleName, Note, SamplePattern, Sync, Tb303, Track, GeneratorTrackType
from py_sonic_pi.transformer import transform


bd_pattern_elements = [
    Sync(n_bars=1),
    Note(65),
    Sleep(1),
    Note(65),
    Sleep(1),
    Note(65),
    Sleep(1),
    Note(65)
]

bass_pattern_elements = [
    Sync(n_bars=1),
    Sleep(0.5),
    Note(40),
    Sleep(1),
    Note(40),
    Sleep(1),
    Note(40),
    Sleep(0.75),
    Note(41)
]

bd_track = GeneratorTrack(id='bd', generator=Sampler(Sample(stock_sample_name=StockSampleName.BD_HAUS)), pattern=SamplePattern(elements=bd_pattern_elements))
bass_track = GeneratorTrack(id='bass', generator=Tb303(), pattern=SamplePattern(elements=bass_pattern_elements),
                            effects=[Reverb(id="bass_reverb")])
bass_bd = GroupTrack(id='bass_bd', children=[bd_track, bass_track], effects=[Reverb(id="bass_bd_reverb", room=1)])


bass_track.gain =0.3
bass_track.pan = 0.5
bass_track.muted = False


master_track = GroupTrack(id='master', children=[bass_bd], effects=[HPFilter(id="masterhpf", cutoff=0.0, controllable=True)])

p = Project(
    top_level_tracks=[master_track],
    beat_length_seconds=0.45
)

lines = transform(p)
with open('output.rb', 'w') as f:
    for line in lines:
        f.write(line + '\n')