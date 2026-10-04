from pathlib import Path

from tests.fixtures import create_fixture_project
from py_sonic_pi.effects import Reverb
from py_sonic_pi.inventory import GroupTrack, Project, StateValue
from py_sonic_pi.transformer import transform

HERE = Path(__file__).parent


def test_something():
    p = create_fixture_project()

    p_serialized = p.serialize()
    p_deserialized = p.deserialize(p_serialized)

    lines_orig = transform([p])
    lines_deserialized = transform([p_deserialized])

    actual = HERE / "generated_project.actual.rb"
    expected = HERE / "generated_project.expected.rb"

    with open(actual, "w") as f:
        for line in lines_orig:
            f.write(line + "\n")

    with open(expected, "r") as f:
        expected_lines = f.read().splitlines()

    assert lines_orig == expected_lines
    assert lines_deserialized == expected_lines


def test_effect_parameters_support_state_values():
    project = create_fixture_project()
    state_value = project.state_values[0]
    effect = Reverb(id="stateful_reverb", room=state_value)
    master_track = project.top_level_tracks[0]
    master_track.custom_effects.append(effect)
    project._set_project_references()

    serialized_project = project.serialize()
    deserialized_project = project.deserialize(serialized_project)

    assert any(
        "room: get(:state_value_test_project_bass_cutoff)" in line
        for line in transform([project])
    )
    assert transform([deserialized_project]) == transform([project])


def test_project_does_not_adopt_state_values_created_after_initialization():
    state_values = StateValue.get_instances()
    project = Project(
        top_level_tracks=[GroupTrack(id="root", children=[])],
        state_values=state_values,
        id="state_snapshot",
    )
    later_state_value = StateValue(
        name="later",
        initial_value=0.0,
        target_value=0.0,
        transition_change_per_bar=0,
    )

    assert later_state_value not in project.state_values
    assert all(state_value.project is project for state_value in project.state_values)
    transform([project])
