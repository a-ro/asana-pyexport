import json

from asanapyexport.wrapper import AsanaAdapter


def export_projects_and_tasks_to_json(token: str, save_file_path: str, is_including_subtasks: bool) -> None:
    """
    Query all projects in Asana and save projects and tasks in JSON file.
    :param token: personal access token in asana
    :param save_file_path: path of file that will contain the exported data
    :param is_including_subtasks: whether to include subtasks or not
    """
    asana = AsanaAdapter(token)
    json_projects = []
    for project, tasks in asana.generate_tasks_per_project(is_including_subtasks=is_including_subtasks):
        json_projects.append(dict(project=project, tasks=tasks))
    with open(save_file_path, "w") as json_file:
        json.dump(json_projects, json_file)
