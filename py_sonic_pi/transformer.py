from jinja2 import Environment, FileSystemLoader
from pathlib import Path

from py_sonic_pi.inventory import Project, TrackType


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
    }
    rendered_content = template.render(**data)
    return rendered_content.splitlines()
