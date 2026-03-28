from py_sonic_pi.inventory import GroupTrack, GeneratorTrack, HPFilter, Pattern, Project, Sample, Sampler, Sleep, StockSampleName, Note, SamplePattern, Sync, Track, GeneratorTrackType
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

bd_track = GeneratorTrack(id='bd', generator=Sampler(Sample(stock_sample_name=StockSampleName.BD_HAUS)), pattern=SamplePattern(elements=bd_pattern_elements))
bass_bd = GroupTrack(id='bass_bd', children=[bd_track], effects=[HPFilter(id="bdhpf", cutoff=100.0)])

master_track = GroupTrack(id='master', children=[bass_bd], effects=[HPFilter(id="masterhpf", cutoff=100.0)])

p = Project(
    top_level_tracks=[master_track],
    beat_length_seconds=0.6
)

lines = transform(p)
with open('output.rb', 'w') as f:
    for line in lines:
        f.write(line + '\n')