from py_sonic_pi.inventory import Project, Transition
from py_sonic_pi.state import load_project_from_state, save_project_to_state



def _set_project_to_fade_out(project: Project, transition: Transition|None) -> None:
    pass

def combine_projects(prev_project: Project, new_project: Project) -> Project:
    pass


def launch(new_project: Project, transition: Transition|None = None) -> None:
    """
    Launches the Sonic Pi project.

    Args:
        project (Project): The Sonic Pi project to launch.
        live_mode (bool): Whether to launch in live mode or not. Defaults to True.
    """
    prev_project = load_project_from_state()
    if prev_project:
        _set_project_to_fade_out(prev_project, transition)

    save_project_to_state(new_project)



