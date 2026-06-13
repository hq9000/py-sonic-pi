from py_sonic_pi.inventory import Note, Pattern, Sleep, Sync
from py_sonic_pi.patterns import (
    _generate_blank_notes_from_matter_line,
    construct_pattern_from_matter,
)


def test_pattern_generation_from_matter():
    matter = """
        sync: 1
        resolution: 0.25
        base_note: C2
        base_pan: 0
        base_amp: 1
        base_attack: 0
        base_decay: 0
        base_sustain: 1.0
        base_release: 0.1 # this is a comment
        base_sustain_amp: 1

        note:    1___0____0___0___0
        amp:     0.77,  0.77,  0.77,  0.77,  0.77
        pan:     0.33,  0.33,  0.33,  0.33,  0.33
        attack:  0.2,  0.2,  0.2,  0.2,  0.2
        decay:   0.1,  0.1,  0.1,  0.1,  0.1
        sustain: 0.9,  0.9,  0.9,  0.9,  0.9
        sustain_amp: 0.8, 0.8, 0.8, 0.8, 0.8
        release: 0.1,0.1,0.1,0.1,0.1
    """
    pattern = construct_pattern_from_matter(matter)

    assert len(pattern.elements) == 10
    assert isinstance(pattern.elements[0], Sync)
    assert pattern.elements[0].n_bars == 1
    assert isinstance(pattern.elements[1], Note)
    assert pattern.elements[1].note == 37
    assert pattern.elements[1].get_attr("amp") == 1.77
    assert pattern.elements[1].get_attr("pan") == 0.33
    assert pattern.elements[1].get_attr("attack") == 0.2
    assert pattern.elements[1].get_attr("decay") == 0.1
    assert pattern.elements[1].get_attr("sustain") == 1.9
    assert pattern.elements[1].get_attr("sustain_amp") == 1.8
    assert pattern.elements[1].get_attr("release") == 0.2
    assert isinstance(pattern.elements[2], Sleep)
    assert pattern.elements[2].duration_beats == 0.75
    assert isinstance(pattern.elements[3], Note)


def test_generate_blank_notes_from_matter_line():
    notes_str = "_1__2,3"
    res = _generate_blank_notes_from_matter_line(notes_str)
    assert len(res) == 5
    assert isinstance(res[0], Sleep)
    assert res[0].duration_beats == 1
    assert res[1].note == 1
    assert isinstance(res[2], Sleep)
    assert res[2].duration_beats == 2
    assert res[3].note == 2
    assert res[4].note == 3
