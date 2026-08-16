from pathlib import Path

from tests.fixtures import create_fixture_project
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
