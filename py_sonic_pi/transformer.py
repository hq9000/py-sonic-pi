from jinja2 import Environment, FileSystemLoader
from pathlib import Path

_INDENT_STEP = 2

from py_sonic_pi.inventory import (
    GeneratorTrack,
    GroupTrack,
    Note,
    Project,
    Sleep,
    Sleep,
    Sync,
    Sync,
    Track,
    GeneratorTrackType,
    EffectInstance,
)


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
        "source_block_lines": _generate_source_block_lines(project),
        "processing_block_lines": _generate_processing_block(project),
        "control_block_lines": _generate_control_block_lines(project),
    }
    rendered_content = template.render(**data)
    return rendered_content.splitlines()


def _generate_processing_block(project: Project) -> list[str]:
    lines = []
    for track in project.top_level_tracks:
        _generate_track_processing_block(track, lines, 0)
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
            comma_separated_parts.append(f"{param}: {value}")

        lines.append(
            f"{' ' * indent}{', '.join(comma_separated_parts)} do |{get_internal_fx_name(fx)}|"
        )
        lines.append(
            f"{' ' * indent}set :{get_internal_fx_name(fx)},{get_internal_fx_name(fx)} if run_count == 1"
        )

    if type(track) == GeneratorTrack:
        lines.append(f"{' ' * indent}{track.id}_loop()")
    elif type(track) == GroupTrack:
        for child_track in track.children:
            _generate_track_processing_block(child_track, lines, indent + _INDENT_STEP)

    for fx in track.get_effects():
        lines.append(f"{' ' * indent}end")


def _generate_source_block_lines(project: Project) -> list[str]:
    lines = []
    for track in project.get_flat_list_of_generator_tracks():
        lines += _generate_source_block_lines_for_one_track(track)
    return lines


def _generate_control_block_lines(project: Project) -> list[str]:

    lines = ["live_loop :control_loop do"]
    lines.append("sync :start_1_bars")

    for fx in project.get_all_controllable_fxs():
        lines.append(f"{' ' * _INDENT_STEP}fx = get(:{get_internal_fx_name(fx)})")
        for param in fx.get_fx_params_dict():
            lines.append(
                f"{' ' * _INDENT_STEP}control fx, {param}: {fx.get_fx_params_dict()[param]}"
            )

    lines.append(f"{' ' * _INDENT_STEP}sleep 1 * get(:beat_length)")
    lines.append("end")
    return lines


def _generate_source_block_lines_for_one_track(track: GeneratorTrack) -> list[str]:
    lines = [f"def {track.id}_loop()"]
    lines.append(f"{' ' * _INDENT_STEP}live_loop :{track.id}_loop do")

    indent = " " * (_INDENT_STEP * 2)

    if track.get_type() == GeneratorTrackType.SYNTH:
        lines.append(f"{indent}use_synth :{track.generator.get_ruby_synth_name()}")

    elements = track.pattern.elements if not track.muted else []

    for element in elements:
        if isinstance(element, Note):
            if track.get_type() == GeneratorTrackType.SAMPLE and element.sample is None:
                line = f"{indent}sample :{track.generator.sample.name.value}"
            elif track.get_type() == GeneratorTrackType.SYNTH:
                line = f"{indent}play {element.note}"

            if element.amp != 1.0:
                line += f", amp: {element.amp}"
            if element.pan != 0.0:
                line += f", pan: {element.pan}"
            if element.attack_beats != 0.0:
                line += f", attack: {element.attack_beats}"
            if element.decay_beats != 0.0:
                line += f", decay: {element.decay_beats}"
            if element.sustain_beats != 0.5:
                line += f", sustain: {element.sustain_beats}"
            if element.release_beats != 0.0:
                line += f", release: {element.release_beats}"
            if element.sample is not None:
                line += f', sample: "{element.sample}"'
            if element.rate != 1.0:
                line += f", rate: {element.rate}"
            lines.append(line)
        elif isinstance(element, Sleep):
            lines.append(f"{indent}sleep {element.duration_beats}*get(:beat_length)")
        elif isinstance(element, Sync):
            lines.append(f"{indent}sync :start_{element.n_bars}_bars")
    lines.append(f"{' ' * (_INDENT_STEP * 2)}end")
    lines.append("end")
    return lines
