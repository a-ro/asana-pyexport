import logging

from asanapyexport.export import export_projects_and_tasks_to_json

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    auth_token = "replace by your token here"
    save_file_path = "save/path/my-asana-data.json"
    export_projects_and_tasks_to_json(auth_token, save_file_path, is_including_subtasks=True)
