from pathlib import Path

from tests.fixtures import create_fixture_project
from py_sonic_pi.transformer import transform

HERE = Path(__file__).parent

def test_something():
    p = create_fixture_project()
    lines = transform(p)
    actual = HERE / "generated_project.actual.rb"
    expected = HERE / "generated_project.expected.rb"

    with open(actual, "w") as f:
        for line in lines:
            f.write(line + "\n")

    with open(expected, "r") as f:
        expected_lines = f.read().splitlines()

    assert lines == expected_lines
