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
    BASE_AMP = "base_amp"
    BASE_PAN = "base_pan"
    BASE_ATTACK = "base_attack"
    BASE_DECAY = "base_decay"
    BASE_SUSTAIN = "base_sustain"
    BASE_RELEASE = "base_release"
    BASE_SUSTAIN_AMP = "base_sustain_amp"
    NOTES = "notes"
    AMPS = "amps"
    PANS = "pans"
    ATTACKS = "attacks"
    DECAYS = "decays"
    SUSTAINS = "sustains"
    RELEASES = "releases"
    SUSTAIN_AMPS = "sustain_amps"


def construct_pattern_from_matter(matter: str) -> Pattern:
    matter = matter.replace(" ", "")
    lines = [
        re.sub(r"#.*", "", line) for line in matter.split("\n") if line.strip() != ""
    ]

    sync = 1
    resolution_beats = 1.0
    base_note = None
    base_amp = None
    base_pan = None
    base_attack = None
    base_decay = None
    base_sustain = None
    base_release = None
    base_sustain_amp = None


    notes_and_sleeps: list[Note | Sleep] = []
    amps = []
    pans = []
    attacks = []
    decays = []
    sustains = []
    releases = []
    sustain_amps = []

    for line in lines:
        if line.startswith(MatterKeywords.SYNC.value + ":"):
            sync = int(line[len(MatterKeywords.SYNC.value) + 1 :])
        elif line.startswith(MatterKeywords.BASE_NOTE.value + ":"):
            base_note = _convert_note_str_to_int(
                line[len(MatterKeywords.BASE_NOTE.value) + 1 :]
            )
        elif line.startswith(MatterKeywords.BASE_AMP.value + ":"):
            base_amp = float(line[len(MatterKeywords.BASE_AMP.value) + 1 :])
        elif line.startswith(MatterKeywords.BASE_ATTACK.value + ":"):
            base_attack = float(line[len(MatterKeywords.BASE_ATTACK.value) + 1 :])
        elif line.startswith(MatterKeywords.BASE_DECAY.value + ":"):
            base_decay = float(line[len(MatterKeywords.BASE_DECAY.value) + 1 :])
        elif line.startswith(MatterKeywords.BASE_SUSTAIN.value + ":"):
            base_sustain = float(line[len(MatterKeywords.BASE_SUSTAIN.value) + 1 :])
        elif line.startswith(MatterKeywords.BASE_RELEASE.value + ":"):
            base_release = float(line[len(MatterKeywords.BASE_RELEASE.value) + 1 :])
        elif line.startswith(MatterKeywords.BASE_SUSTAIN_AMP.value + ":"):
            base_sustain_amp = float(
                line[len(MatterKeywords.BASE_SUSTAIN_AMP.value) + 1 :]
            )
        elif line.startswith(MatterKeywords.BASE_PAN.value + ":"):
            base_pan = float(line[len(MatterKeywords.BASE_PAN.value) + 1 :])
        elif line.startswith(MatterKeywords.NOTES.value + ":"):
            notes_and_sleeps = _generate_blank_notes_from_matter_line(
                line[len(MatterKeywords.NOTES.value) + 1 :]
            )
        elif line.startswith(MatterKeywords.AMPS.value + ":"):
            amps = [
                float(amp_str.strip())
                for amp_str in line[len(MatterKeywords.AMPS.value) + 1 :].split(",")
            ]
        elif line.startswith(MatterKeywords.PANS.value + ":"):
            pans = [
                float(pan_str.strip())
                for pan_str in line[len(MatterKeywords.PANS.value) + 1 :].split(",")
            ]
        elif line.startswith(MatterKeywords.ATTACKS.value + ":"):
            attacks = [
                float(attack_str.strip())
                for attack_str in line[len(MatterKeywords.ATTACKS.value) + 1 :].split(
                    ","
                )
            ]
        elif line.startswith(MatterKeywords.DECAYS.value + ":"):
            decays = [
                float(decay_str.strip())
                for decay_str in line[len(MatterKeywords.DECAYS.value) + 1 :].split(",")
            ]
        elif line.startswith(MatterKeywords.SUSTAINS.value + ":"):
            sustains = [
                float(sustain_str.strip())
                for sustain_str in line[len(MatterKeywords.SUSTAINS.value) + 1 :].split(
                    ","
                )
            ]
        elif line.startswith(MatterKeywords.RELEASES.value + ":"):
            releases = [
                float(release_str.strip())
                for release_str in line[len(MatterKeywords.RELEASES.value) + 1 :].split(
                    ","
                )
            ]
        elif line.startswith(MatterKeywords.SUSTAIN_AMPS.value + ":"):
            sustain_amps = [
                float(sustain_amp_str.strip())
                for sustain_amp_str in line[
                    len(MatterKeywords.SUSTAIN_AMPS.value) + 1 :
                ].split(",")
            ]
        elif line.startswith(MatterKeywords.RESOLUTION.value + ":"):
            resolution_beats = float(line[len(MatterKeywords.RESOLUTION.value) + 1 :])
            pass
        else:
            raise ValueError(f"Unknown matter keyword in line: {line}")

    notes = [element for element in notes_and_sleeps if isinstance(element, Note)]

    for note in notes:
        if base_note is not None:
            note.note += base_note
        if base_amp is not None:
            note.amp = base_amp
        if base_attack is not None:
            note.attack_beats = base_attack
        if base_decay is not None:
            note.decay_beats = base_decay
        if base_sustain is not None:
            note.sustain_beats = base_sustain
        if base_sustain_amp is not None:
            note.sustain_amp = base_sustain_amp
        if base_release is not None:
            note.release_beats = base_release
        if base_pan is not None:
            note.pan = base_pan

    if len(amps) and len(amps) != len(notes):
        raise ValueError(
            "Length of amps list must be either 0 or equal to the number of notes"
        )
    if len(pans) and len(pans) != len(notes):
        raise ValueError(
            "Length of pans list must be either 0 or equal to the number of notes"
        )
    if len(attacks) and len(attacks) != len(notes):
        raise ValueError(
            "Length of attacks list must be either 0 or equal to the number of notes"
        )
    if len(decays) and len(decays) != len(notes):
        raise ValueError(
            "Length of decays list must be either 0 or equal to the number of notes"
        )
    if len(sustains) and len(sustains) != len(notes):
        raise ValueError(
            "Length of sustains list must be either 0 or equal to the number of notes"
        )
    if len(releases) and len(releases) != len(notes):
        raise ValueError(
            "Length of releases list must be either 0 or equal to the number of notes"
        )
    if len(sustain_amps) and len(sustain_amps) != len(notes):
        raise ValueError(
            "Length of sustain_amps list must be either 0 or equal to the number of notes"
        )

    sleeps = [element for element in notes_and_sleeps if isinstance(element, Sleep)]
    for sleep in sleeps:
        sleep.duration_beats = resolution_beats * sleep.duration_beats

    for i in range(len(notes)):
        if i < len(amps):
            notes[i].amp = amps[i]
        if i < len(pans):
            notes[i].pan = pans[i]
        if i < len(attacks):
            notes[i].attack_beats = attacks[i]
        if i < len(decays):
            notes[i].decay_beats = decays[i]
        if i < len(sustains):
            notes[i].sustain_beats = sustains[i]
        if i < len(releases):
            notes[i].release_beats = releases[i]
        if i < len(sustain_amps):
            notes[i].sustain_amp = sustain_amps[i]

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
            if note_str.strip() != "":
                res.append(Note(note=int(note_str.strip())))
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
