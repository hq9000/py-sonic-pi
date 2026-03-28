from py_sonic_pi.inventory import GroupTrack, GeneratorTrack, HPFilter, Pattern, Project, Sample, Sampler, StockSampleName, Note, SamplePattern, Track
from py_sonic_pi.transformer import transform


bd_pattern_elements = [
    Note(65),
]

bd_track = GeneratorTrack(id='bd', generator=Sampler(Sample(stock_sample_name=StockSampleName.BD_HAUS)), pattern=SamplePattern(elements=bd_pattern_elements))
bass_bd = GroupTrack(id='bass_bd', children=[bd_track], effects=[HPFilter(id="bdhpf", cutoff=100.0)])

master_track = GroupTrack(id='master', children=[bass_bd], effects=[HPFilter(id="masterhpf", cutoff=100.0)])

p = Project(
    top_level_tracks=[master_track],
    beat_length_seconds=0.6
)

lines = transform(p)
for line in lines:
    print(line)