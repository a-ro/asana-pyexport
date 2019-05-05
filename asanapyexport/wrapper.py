from typing import Iterator

import asana

from asanapyexport.util import user_selection


class AsanaAdapter:
    def __init__(self, token, page_size=100):
        self.client = asana.Client.access_token(token)
        self.client.options["page_size"] = page_size

    def select_workspace(self) -> str:
        workspaces = self.client.workspaces.find_all()
        workspace = user_selection("Please choose a workspace", workspaces)
        workspace_id = workspace["id"]
        return workspace_id

    def get_projects(self, workspace_id: str) -> Iterator:
        projects = self.client.projects.find_all(
            {
                "workspace": workspace_id,
                "opt_expand": "owner, team, members, start_on, created_at, modified_at, archived, custom_fields, notes",
            }
        )
        return projects

    def get_tasks(self, project_id: str) -> Iterator:
        # Using opt_expand and opt_fields makes opt_fields overwrite opt_expand.
        # Didn't find a way to solve it so I only used opt_expand instead.
        tasks = self.client.tasks.find_by_project(
            project_id,
            {
                "opt_expand": "name, assignee, id, due_on, created_at, modified_at, completed, completed_at,"
                " assignee, assignee_status, parent, notes, dependencies"
            },
        )
        return tasks

    def get_sub_tasks(self, task_id):
        subtasks = self.client.request(
            "get",
            f"/tasks/{task_id}/subtasks?opt_expand=name,id,due_on,created_at,modified_at,completed,completed_at,"
            f"assignee,assignee_status",
        )
        return subtasks

    def generate_tasks_per_project(self, is_including_subtasks: bool) -> Iterator:
        workspace_id = self.select_workspace()
        project_iterator = self.get_projects(workspace_id)
        for project in project_iterator:
            task_iterator = self.get_tasks(project["id"])
            if is_including_subtasks:
                tasks = self.__create_tasks_with_subtasks(task_iterator)
            else:
                tasks = list(task_iterator)
            yield project, tasks

    def __create_tasks_with_subtasks(self, task_iterator):
        tasks = []
        for task in task_iterator:
            task["sub_tasks"] = list(self.get_sub_tasks(task["id"]))
            tasks.append(task)
        return tasks
