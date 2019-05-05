import json
import logging

from asanapyexport.wrapper import AsanaAdapter


def export_projects_and_tasks_to_json(token: str, save_file_path: str) -> None:
    asana = AsanaAdapter(token)
    json_projects = []
    for project, task_iterator in asana.generate_tasks_per_project():
        logging.info(f"processing project: {project['name']}")
        tasks = list(task_iterator)
        json_projects.append(dict(project=project, tasks=tasks))
    with open(save_file_path, "w") as json_file:
        json.dump(json_projects, json_file)
