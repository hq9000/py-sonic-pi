from pathlib import Path

from py_sonic_pi.inventory import Project
from py_sonic_pi.transformer import transform


_SERIALIZED_PLAYING_PROJECT_FILE_NAME = "playing.json"
_OUTPUT_RB_FILE_NAME = "last.rb"

class TransitionManager:
    def __init__(self, working_directory: str):
        self.working_directory = working_directory

    def do_transition(self, new_project: Project, transition_time_bars: float) -> None:
        old_project = self._load_project_from_serialized_file(_SERIALIZED_PLAYING_PROJECT_FILE_NAME)
        self._save_serialized_project_to_file(new_project, _SERIALIZED_PLAYING_PROJECT_FILE_NAME)
        if not old_project:
            new_project.save_references = True
        if not old_project or old_project.id == new_project.id:
            self._render_projects_to_rb_file([new_project], _OUTPUT_RB_FILE_NAME)
            return

        old_project.fade_out(transition_time_bars)
        new_project.fade_in(transition_time_bars)
        new_project.save_references = True
        self._render_projects_to_rb_file([old_project, new_project], _OUTPUT_RB_FILE_NAME)

    def _render_projects_to_rb_file(self, projects: list[Project], file_path: str) -> None:
        lines = transform(projects)
        with open(file_path, "w") as f:
            for line in lines:
                f.write(line + "\n")

    def _save_serialized_project_to_file(self, project: Project, file_path: str) -> None:
        serialized_project = project.serialize()
        with open(file_path, "w") as f:
            f.write(serialized_project)

    def _load_project_from_serialized_file(self, file_path: str) -> Project | None:
        if not Path(file_path).exists():
            return None
        with open(file_path, "r") as f:
            serialized_project = f.read()
        return Project.deserialize(serialized_project)
