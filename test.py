from py_sonic_pi.inventory import HPFilter, Pattern, Project, Sample, SampleName, Track
from py_sonic_pi.transformer import transform

bd_track = Track(generator=Sample(name=SampleName.BD_HAUS), pattern=Pattern(raw="x---x---x---x---"))



p = Project(tracks=[], master_effects=[HPFilter(cutoff=100.0, resonance=0.5)])

print(transform(p))