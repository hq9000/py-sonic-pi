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
    Project,
)

_INDENT_STEP = 2
_GLOBAL_GAIN_ACTIVATION_THRESHOLD = 0.01

def transform(projects: list[Project]) -> list[str]:
    # Get the directory of the current file
    current_dir = Path(__file__).parent
    # Templates are in the 'templates' subfolder relative to this file's dir
    templates_dir = current_dir / "templates"
    env = Environment(loader=FileSystemLoader(str(templates_dir)))
    template = env.get_template("project.template.rb")

    data = {
        "beat_length_seconds": projects[-1].beat_length_seconds,
        "TrackType": GeneratorTrackType,
        "state_declaration_block_lines": _generate_state_declaration_lines(projects),
        "source_block_lines": _generate_source_block_lines(projects),
        "processing_block_lines": _generate_processing_block(projects),
        "fx_control_block_lines": _generate_fx_control_block_lines(projects),
        "state_control_block_lines": _generate_state_control_block_lines(projects),
    }
    rendered_content = template.render(**data)
    return rendered_content.splitlines()


def transform_to_file(projects: list[Project], output_file_path: str) -> None:
    lines = transform(projects)
    with open(output_file_path, "w") as f:
        f.write("\n".join(lines))

def _generate_guard_lines(project: Project) -> list[str]:
    return [
        f"{' ' * (_INDENT_STEP * 3)}if get(:{project.get_master_gain_state_value().get_ruby_state_value_name()}) <= {_GLOBAL_GAIN_ACTIVATION_THRESHOLD}",
        f"{' ' * (_INDENT_STEP * 4)}stop",
        f"{' ' * (_INDENT_STEP * 3)}end"
    ]


def _generate_processing_block(projects: list[Project]) -> list[str]:
    lines = []
    for project in projects:
        _generate_track_processing_block(project=project, track=project.master_track, lines=lines, indent=0)
    return lines


def get_internal_fx_name(fx: EffectInstance) -> str:
    return f"fxname_{fx.get_ruby_effect_name()}_{fx.project.id}_{fx.id}"


def _generate_track_processing_block(
    project: Project, track: Track, lines: list[str], indent: int
) -> None:
    lines.append(f"{' ' * indent}# Track: {track.id}")
    for fx in track.get_effects():
        comma_separated_parts = [
            f"with_fx :{fx.get_ruby_effect_name()}",
        ]

        for param, value in fx.get_fx_params_dict().items():
            if isinstance(value, StateValue):
                comma_separated_parts.append(
                    f"{param}: get(:{value.get_ruby_state_value_name()})"
                )
            else:
                comma_separated_parts.append(f"{param}: {value}")

        lines.append(
            f"{' ' * indent}{', '.join(comma_separated_parts)} do |{get_internal_fx_name(fx)}|"
        )


        lines.append(
            f"{' ' * indent}set :{get_internal_fx_name(fx)},{get_internal_fx_name(fx)} if run_count == 1"
        )

    if isinstance(track, GeneratorTrack):
        lines.append(f"{' ' * indent}{_get_live_loop_name_for_track(track)}()")
    elif isinstance(track, GroupTrack):
        for child_track in track.children:
            _generate_track_processing_block(project=project, track=child_track, lines=lines, indent=indent + _INDENT_STEP)

    for fx in track.get_effects():
        lines.append(f"{' ' * indent}end")


def _generate_state_declaration_lines(projects: list[Project]) -> list[str]:
    lines = []

    for project in projects:
        for state_value in project.state_values:
            lines.append(
                f"set :{state_value.get_ruby_state_value_name()}, {state_value.initial_value} if run_count == 1"
            )
    return lines

def _generate_state_control_block_lines(projects: list[Project]) -> list[str]:
    lines = []
    for project in projects:
        lines += _generate_state_control_block_lines_for_one_project(project)
    return lines

def _generate_state_control_block_lines_for_one_project(project: Project) -> list[str]:
    lines = [f"live_loop :state_management_loop_{project.id} do"]
    lines.append("sync :start_1_bars")
    lines.extend(
        _generate_guard_lines(project)
    )

    for state_value in project.state_values:
        if state_value.transition_change_per_bar > 0:
            # if get(:state_value.name) < state_value.target_value, then increase it by transition_change_per_bar, but do not exceed target_value
            # conversely, if target_value < initial_value, then decrease it by transition_change_per_bar, but do not go below target_value
            # in sonic-pi, it should look like this:
            # set :state_value.name, [get(:state_value.name) + transition_change_per_bar, state_value.target_value].min
            # if target_value < get(:state_value.name)
            #   set :state_value.name, [get(:state_value.name) - transition_change_per_bar, state_value.target_value].max
            # elseif target_value > get(:state_value.name)
            #  set :state_value.name, [get(:state_value.name) + transition_change_per_bar, state_value.target_value].min

            lines.append(
                f"if get(:{state_value.get_ruby_state_value_name()}) < {state_value.target_value}"
            )
            lines.append(
                f"  set :{state_value.get_ruby_state_value_name()}, [get(:{state_value.get_ruby_state_value_name()}) + {state_value.transition_change_per_bar}, {state_value.target_value}].min"
            )
            lines.append(
                f"elsif get(:{state_value.get_ruby_state_value_name()}) > {state_value.target_value}"
            )
            lines.append(
                f"  set :{state_value.get_ruby_state_value_name()}, [get(:{state_value.get_ruby_state_value_name()}) - {state_value.transition_change_per_bar}, {state_value.target_value}].max"
            )
            lines.append("end")

        else:
            lines.append(
                f"set :{state_value.get_ruby_state_value_name()}, {state_value.target_value}"
            )

    lines.append("sleep 0.25")
    lines.append("end")
    return lines


def _generate_source_block_lines(projects: list[Project]) -> list[str]:
    lines = []
    for project in projects:
        for track in project.get_flat_list_of_generator_tracks():
            lines += _generate_source_block_lines_for_one_track(track)
    return lines

def _generate_fx_control_block_lines(projects: list[Project]) -> list[str]:
    lines = []
    for project in projects:
        lines += _generate_fx_control_block_lines_for_one_project(project)
    return lines

def _generate_fx_control_block_lines_for_one_project(project: Project) -> list[str]:

    lines = [f"live_loop :control_loop_{project.id} do"]
    lines.append("sync :start_1_bars")
    lines.extend(
        _generate_guard_lines(project)
    )
    lines.append(f"{' ' * _INDENT_STEP}if run_count != 1")
    for fx in project.get_all_controllable_fxs():
        lines.append(f"{' ' * 2 * _INDENT_STEP}fx = get(:{get_internal_fx_name(fx)})")
        for param in fx.get_fx_params_dict():
            val = fx.get_fx_params_dict()[param]
            if isinstance(val, StateValue):
                val = f"get(:{val.get_ruby_state_value_name()})"
            else:
                val = f"{val}"
            lines.append(f"{' ' * 2 * _INDENT_STEP}control fx, {param}: {val}")

    lines.append(f"{' ' * _INDENT_STEP}sleep 1 * get(:beat_length)")
    lines.append(f"{' ' * _INDENT_STEP}end")
    lines.append("end")
    return lines

def _get_live_loop_name_for_track(track: GeneratorTrack) -> str:
    return f"{track.project.id}_{track.id}_loop"

def _generate_source_block_lines_for_one_track(
    track: GeneratorTrack
) -> list[str]:
    live_loop_name = _get_live_loop_name_for_track(track)
    lines = [f"def {live_loop_name}()"]
    lines.append(f"{' ' * _INDENT_STEP}live_loop :{live_loop_name} do")

    indent = " " * (_INDENT_STEP * 3)

    if track.get_type() == GeneratorTrackType.SYNTH:
        lines.append(f"{indent}use_synth :{track.generator.get_ruby_synth_name()}")

    elements = track.pattern.elements if not track.muted else []

    if not elements:
        raise ValueError(f"Track {track.id} has no elements in its pattern.")

    if not isinstance(elements[0], Sync):
        raise ValueError(f"Track {track.id} pattern must start with a Sync element.")

    lines.append(f"{indent}sync :start_{elements[0].n_bars}_bars")
    lines.extend(
        _generate_guard_lines(track.project)
    )
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
                        value_str = f"get(:{value.get_ruby_state_value_name()})"
                    else:
                        raise ValueError(
                            f"Unsupported parameter value type: {type(value)}"
                        )
                    line += f", {param}: {value_str}"

            lines.append(line)
        elif isinstance(element, Sleep):
            lines.append(f"{indent}sleep {element.duration_beats}*get(:beat_length)")
    lines.append(f"{' ' * (_INDENT_STEP * 2)}end")
    lines.append("end")
    return lines
