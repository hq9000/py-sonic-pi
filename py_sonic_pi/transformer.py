from jinja2 import Environment, FileSystemLoader
from pathlib import Path

from py_sonic_pi.inventory import GeneratorTrack, GroupTrack, Project, Track, TrackType, EffectInstance


def transform(project: Project) -> list[str]:
    # Get the directory of the current file
    current_dir = Path(__file__).parent
    # Templates are in the 'templates' subfolder relative to this file's dir
    templates_dir = current_dir / 'templates'
    env = Environment(loader=FileSystemLoader(str(templates_dir)))
    template = env.get_template('project.template.rb')

    data = {
        "project": project,
        "TrackType": TrackType,
        "processing_block_lines": _generate_processing_block(project)
    }
    rendered_content = template.render(**data)
    return rendered_content.splitlines()

def _generate_processing_block(project: Project) -> list[str]:
    lines = []
    for track in project.top_level_tracks:
        _generate_track_block(track, lines, 0)
    return lines

def get_internal_fx_name(fx: EffectInstance) -> str:
    return f"{fx.get_ruby_effect_name()}_{fx.id}"

def _generate_track_block(track: Track, lines: list[str], indent: int) -> None:
    lines.append(f"{' ' * indent}# Track: {track.id}")
    for fx in track.effects:
        comma_separated_parts = [
            f"with_fx :{fx.get_ruby_effect_name()}",
        ]

        for param, value in fx.get_fx_params_dict().items():
            comma_separated_parts.append(f"{param}: {value}")

        lines.append(f"{' ' * indent}{', '.join(comma_separated_parts)} do |{ get_internal_fx_name(fx) }|")
        lines.append(f"{' ' * indent}set :{get_internal_fx_name(fx)},{get_internal_fx_name(fx)} if run_count == 1")

    if type(track) == GeneratorTrack:
        lines.append(f"{' ' * indent}{track.id}_loop()")
    elif type(track) == GroupTrack:
        for child_track in track.children:
            _generate_track_block(child_track, lines, indent + 4)

    for fx in track.effects:
        lines.append(f"{' ' * indent}end")
