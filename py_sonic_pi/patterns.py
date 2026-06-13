from enum import Enum
import re

from py_sonic_pi.inventory import Note, Pattern, PatternElement, Sleep, Sync

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

        notes:    0___0___0___0___0
        amps:     1,  1,  1,  1,  1
        pans:     0,  0,  0,  0,  0
        attacks:  0,  0,  0,  0,  0
        decays:   0,  0,  0,  0,  0
        sustains: 1,  1,  1,  1,  1
        sustain_amps: 1, 1, 1, 1, 1
        releases: 0.1,0.1,0.1,0.1,0.1
    """


class MatterKeywords(Enum):
    SYNC = "sync"
    RESOLUTION = "resolution"
    BASE_NOTE = "base_note"
    NOTE = "note"


def construct_pattern_from_matter(matter: str) -> Pattern:
    matter = matter.replace(" ", "")
    lines = [
        re.sub(r"#.*", "", line) for line in matter.split("\n") if line.strip() != ""
    ]

    sync = 1
    resolution_beats = 1.0
    base_note = None

    notes_and_sleeps: list[Note | Sleep] = []
    generic_bases: dict[str, float] = {}
    generic_values: dict[str, list[float]] = {}

    for line in lines:
        if line.startswith(MatterKeywords.SYNC.value + ":"):
            sync = int(line[len(MatterKeywords.SYNC.value) + 1 :])
        elif line.startswith(MatterKeywords.BASE_NOTE.value + ":"):
            base_note = _convert_note_str_to_int(
                line[len(MatterKeywords.BASE_NOTE.value) + 1 :]
            )
        elif line.startswith(MatterKeywords.NOTE.value + ":"):
            notes_and_sleeps = _generate_blank_notes_from_matter_line(
                line[len(MatterKeywords.NOTE.value) + 1 :]
            )
        elif line.startswith(MatterKeywords.RESOLUTION.value + ":"):
            resolution_beats = float(line[len(MatterKeywords.RESOLUTION.value) + 1 :])
        # Generic case
        elif line.startswith("base_"):
            name = line.split(":")[0].strip()
            name = name[len("base_") :]
            value_str = line[len("base_" + name) + 1 :].strip()
            generic_bases[name] = float(value_str)
        elif line.count(":") == 1:
            name = line.split(":")[0].strip()
            values_str = line[len(name) + 1 :].strip()
            generic_values[name] = [
                float(val_str.strip())
                for val_str in values_str.split(",")
            ]
        else:
            raise ValueError(f"unrecognizable matter line: {line}")

    notes = [element for element in notes_and_sleeps if isinstance(element, Note)]

    for note in notes:
        if base_note is not None:
            note.note += base_note

    for attr_name in generic_values.keys():
        if attr_name not in generic_bases:
            generic_bases[attr_name] = 0.0

        if len(generic_values[attr_name]) and len(generic_values[attr_name]) != len(notes):
            raise ValueError(
                f"Length of {attr_name} list must be either 0 or equal to the number of notes"
            )

    if sorted(generic_bases.keys()) != sorted(generic_values.keys()):
        raise ValueError(
            f"Generic base keys must match generic value keys. Got bases: {generic_bases.keys()}, values: {generic_values.keys()}"
        )

    sleeps = [element for element in notes_and_sleeps if isinstance(element, Sleep)]
    for sleep in sleeps:
        sleep.duration_beats = resolution_beats * sleep.duration_beats

    for i in range(len(notes)):
            for attr_name in generic_bases.keys():
                if i < len(generic_values[attr_name]):
                    notes[i].set_attr(attr_name, generic_bases[attr_name] + generic_values[attr_name][i])

    elements: list[PatternElement] = []
    elements.append(Sync(n_bars=sync))
    elements.extend(notes_and_sleeps)

    if elements[-1] and isinstance(elements[-1], Sleep):
        elements.pop()

    return Pattern(elements=elements)


def _generate_blank_notes_from_matter_line(notes_str: str) -> list[Note | Sleep]:
    """
    1__2,3__4,5___6
    """
    note_blocks = re.split(r"_+", notes_str)
    pause_blocks = re.findall(r"_+", notes_str)

    res = []

    for note_block, pause_block in zip(note_blocks, pause_blocks + [""]):
        for note_str in note_block.split(","):

            note_str = note_str.strip()
            if note_str != "":
                res.append(Note(note=int(note_str)))
        if pause_block != "":
            res.append(Sleep(duration_beats=len(pause_block)))

    return res


def _convert_note_str_to_int(note_str: str) -> int:

    note_str = note_str.strip()
    if note_str == "":
        raise ValueError("Empty note string")

    try:
        res = int(note_str)
        return res
    except ValueError:
        pass

    match = re.match(r"([A-Ga-g])([#b]?)(-?\d+)", note_str)
    if not match:
        raise ValueError(f"Invalid note string: {note_str}")

    note_name, accidental, octave_str = match.groups()
    note_name = note_name.upper()
    octave = int(octave_str)

    base_note = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}[note_name]

    if accidental == "#":
        base_note += 1
    elif accidental == "b":
        base_note -= 1

    return base_note + (octave + 1) * 12
