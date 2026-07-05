from jinja2 import Environment, FileSystemLoader
from pathlib import Path

from py_sonic_pi.patterns import MatterKeywords
from py_sonic_pi.inventory import (
    GeneratorTrack,
    GroupTrack,
    Note,
    Sleep,
    StateValue,
    Sync,
    Track,
    GeneratorTrackType,
    EffectInstance,
)
from py_sonic_pi.project import Project

_INDENT_STEP = 2


def transform(project: Project) -> list[str]:
    # Get the directory of the current file
    current_dir = Path(__file__).parent
    # Templates are in the 'templates' subfolder relative to this file's dir
    templates_dir = current_dir / "templates"
    env = Environment(loader=FileSystemLoader(str(templates_dir)))
    template = env.get_template("project.template.rb")

    data = {
        "project": project,
        "TrackType": GeneratorTrackType,
        "state_declaration_block_lines": _generate_state_declaration_lines(project),
        "source_block_lines": _generate_source_block_lines(project),
        "processing_block_lines": _generate_processing_block(project),
        "fx_control_block_lines": _generate_fx_control_block_lines(project),
        "state_control_block_lines": _generate_state_control_block_lines(project),
    }
    rendered_content = template.render(**data)
    return rendered_content.splitlines()


def transform_to_file(project: Project, output_file_path: str) -> None:
    lines = transform(project)
    with open(output_file_path, "w") as f:
        f.write("\n".join(lines))


def _generate_processing_block(project: Project) -> list[str]:
    lines = []
    _generate_track_processing_block(project.master_track, lines, 0)
    return lines


def get_internal_fx_name(fx: EffectInstance) -> str:
    return f"{fx.get_ruby_effect_name()}_{fx.id}"


def _generate_track_processing_block(
    track: Track, lines: list[str], indent: int
) -> None:
    lines.append(f"{' ' * indent}# Track: {track.id}")
    for fx in track.get_effects():
        comma_separated_parts = [
            f"with_fx :{fx.get_ruby_effect_name()}",
        ]

        for param, value in fx.get_fx_params_dict().items():
            if isinstance(value, StateValue):
                comma_separated_parts.append(f"{param}: get(:{value.name})")
            else:
                comma_separated_parts.append(f"{param}: {value}")

        lines.append(
            f"{' ' * indent}{', '.join(comma_separated_parts)} do |{get_internal_fx_name(fx)}|"
        )
        lines.append(
            f"{' ' * indent}set :{get_internal_fx_name(fx)},{get_internal_fx_name(fx)} if run_count == 1"
        )

    if isinstance(track, GeneratorTrack):
        lines.append(f"{' ' * indent}{track.id}_loop()")
    elif isinstance(track, GroupTrack):
        for child_track in track.children:
            _generate_track_processing_block(child_track, lines, indent + _INDENT_STEP)

    for fx in track.get_effects():
        lines.append(f"{' ' * indent}end")


def _generate_state_declaration_lines(project: Project) -> list[str]:
    lines = []
    for state_value in project.state_values:
        lines.append(
            f"set :{state_value.name}, {state_value.initial_value} if run_count == 1"
        )
    return lines

def _generate_state_control_block_lines(project: Project) -> list[str]:
    lines = ["live_loop :state_management_loop do"]
    lines.append("sync :start_1_bars")

    for state_value in project.state_values:
        if state_value.transition_change_per_bar > 0:
            if state_value.target_value >= state_value.initial_value:
                lines.append(
                    f"set :{state_value.name}, [get(:{state_value.name}) + {state_value.transition_change_per_bar}, {state_value.target_value}].min"
                )
            else:
                lines.append(
                    f"set :{state_value.name}, [get(:{state_value.name}) - {state_value.transition_change_per_bar}, {state_value.target_value}].max"
                )
        else:
            lines.append(
                f"set :{state_value.name}, {state_value.target_value}"
            )

    lines.append("sleep 0.25")
    lines.append("end")
    return lines


def _generate_source_block_lines(project: Project) -> list[str]:
    lines = []
    for track in project.get_flat_list_of_generator_tracks():
        lines += _generate_source_block_lines_for_one_track(track)
    return lines


def _generate_fx_control_block_lines(project: Project) -> list[str]:

    lines = ["live_loop :control_loop do"]
    lines.append("sync :start_1_bars")
    lines.append(f"{' ' * _INDENT_STEP}if run_count != 1")
    for fx in project.get_all_controllable_fxs():
        lines.append(f"{' ' * 2 * _INDENT_STEP}fx = get(:{get_internal_fx_name(fx)})")
        for param in fx.get_fx_params_dict():
            val = fx.get_fx_params_dict()[param]
            if isinstance(val, StateValue):
                val = f"get(:{val.name})"
            else:
                val = f"{val}"
            lines.append(
                f"{' ' * 2 * _INDENT_STEP}control fx, {param}: {val}"
            )

    lines.append(f"{' ' * _INDENT_STEP}sleep 1 * get(:beat_length)")
    lines.append(f"{' ' * _INDENT_STEP}end")
    lines.append("end")
    return lines


def _generate_source_block_lines_for_one_track(track: GeneratorTrack) -> list[str]:
    lines = [f"def {track.id}_loop()"]
    lines.append(f"{' ' * _INDENT_STEP}live_loop :{track.id}_loop do")

    indent = " " * (_INDENT_STEP * 3)

    if track.get_type() == GeneratorTrackType.SYNTH:
        lines.append(f"{indent}use_synth :{track.generator.get_ruby_synth_name()}")

    elements = track.pattern.elements if not track.muted else []

    if not elements:
        raise ValueError(f"Track {track.id} has no elements in its pattern.")

    if not isinstance(elements[0], Sync):
        raise ValueError(
            f"Track {track.id} pattern must start with a Sync element."
        )


    lines.append(f"{indent}sync :start_{elements[0].n_bars}_bars")
    lines.append(f"{' ' * (_INDENT_STEP * 3)}if get(:internal_master_gain) >= 0.01")
    indent = " " * (_INDENT_STEP * 4)
    for element in elements:
        if isinstance(element, Note):
            if track.get_type() == GeneratorTrackType.SAMPLE and element.sample is None:
                line = f"{' ' * (_INDENT_STEP * 4)}sample :{track.generator.sample.name.value}"
            elif track.get_type() == GeneratorTrackType.SYNTH:
                line = f"{indent}play {element.note}"
                # Combine synth parameters and note attributes, with note attributes taking precedence
                all_params = {}
                # Get all synth parameters using public methods
                for param_name in track.generator.get_parameter_names():
                    all_params[param_name] = (
                        track.generator.get_parameter_value_by_name(param_name)
                    )
                for name, value in element.attributes.items():
                    if name == MatterKeywords.NOTE.value:
                        continue
                    all_params[name] = value

                for param, value in all_params.items():
                    if isinstance(value, float) or isinstance(value, int):
                        value_str = f"{value}"
                    elif isinstance(value, StateValue):
                        value_str = f"get(:{value.name})"
                    else:
                        raise ValueError(f"Unsupported parameter value type: {type(value)}")
                    line += f", {param}: {value_str}"

            lines.append(line)
        elif isinstance(element, Sleep):
            lines.append(f"{indent}sleep {element.duration_beats}*get(:beat_length)")
    lines.append(f"{' ' * (_INDENT_STEP * 3)}else")
    lines.append(f"{' ' * (_INDENT_STEP * 4)}sleep 0.25")
    lines.append(f"{' ' * (_INDENT_STEP * 3)}end")
    lines.append(f"{' ' * (_INDENT_STEP * 2)}end")
    lines.append("end")
    return lines
