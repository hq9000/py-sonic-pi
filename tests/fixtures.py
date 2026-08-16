from py_sonic_pi.effects import HPFilter, Reverb
from py_sonic_pi.inventory import (
    GroupTrack,
    GeneratorTrack,
    Sample,
    Sampler,
    StateValue,
    StockSampleName,
    Project,
)

from py_sonic_pi.patterns import construct_pattern_from_matter
from py_sonic_pi.synths import Saw, Tb303


def create_fixture_project():

    bass_cutoff = StateValue(
        name="bass_cutoff",
        initial_value=50,
        target_value=100,
        transition_change_per_bar=5,
    )

    bd_pattern = construct_pattern_from_matter(
        """
            sync: 1
            resolution: 0.25
            note: 0____0____0____0
        """
    )

    oh_pattern = construct_pattern_from_matter(
        """
            sync: 1
            resolution: 0.25
            note: __0____0____0____0
        """
    )

    bass_pattern = construct_pattern_from_matter(
        """
            sync: 1
            resolution: 0.25
            base_note: C3
            base_release: 0.1
            note: _0__12__1__0_
        """
    )

    sub_bass_pattern = construct_pattern_from_matter(
        """
            sync: 1
            resolution: 0.25
            base_note: C1
            base_release: 0.6
            note: 0______0____0____0
        """
    )

    bd_track = GeneratorTrack(
        id="bd",
        generator=Sampler(Sample(stock_sample_name=StockSampleName.BD_HAUS)),
        pattern=bd_pattern,
    )

    oh_track = GeneratorTrack(
        id="oh",
        amp=0.2,
        generator=Sampler(Sample(stock_sample_name=StockSampleName.DRUM_CYMBAL_OPEN)),
        pattern=oh_pattern,
    )

    crash_track = GeneratorTrack(
        id="crash",
        generator=Sampler(Sample(stock_sample_name=StockSampleName.RIDE_TRI)),
        amp=0.5,
        pattern=construct_pattern_from_matter(
            """
            sync: 2
            note: 0
            """
        ),
    )
    snare_track = GeneratorTrack(
        id="snare",
        generator=Sampler(Sample(stock_sample_name=StockSampleName.ELEC_SNARE)),
        amp=0.4,
        pattern=construct_pattern_from_matter(
            """
            sync: 1
            note: _0__0
            """
        ),
    )

    bass_synth = Tb303()
    bass_synth.set_parameter_value("amp", 1.3)
    bass_synth.set_cutoff(bass_cutoff)
    bass_synth.set_cutoff_slide(20)

    sub_bass_synth = Saw()
    sub_bass_synth.set_pan(-1)

    bass_track = GeneratorTrack(
        id="bass",
        generator=bass_synth,
        pattern=bass_pattern,
        effects=[Reverb(id="bass_reverb")],
    )
    sub_bass_track = GeneratorTrack(
        id="sub_bass",
        generator=sub_bass_synth,
        pattern=sub_bass_pattern,
        effects=[],
        amp=1,
    )
    bass_bd = GroupTrack(
        id="bass_bd",
        children=[bd_track, bass_track, sub_bass_track],
        effects=[],
    )

    master_track = GroupTrack(
        id="master",
        children=[bass_bd, crash_track, snare_track, oh_track],
        effects=[HPFilter(id="masterhpf", cutoff=0.0, controllable=True)],
    )

    p = Project(
        top_level_tracks=[master_track],
        beat_length_seconds=0.45,
        state_values=[bass_cutoff],
        id="test_project",
    )
    p.fade_out(6)
    return p
