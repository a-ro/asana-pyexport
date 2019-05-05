from typing import Iterator

import asana

from asanapyexport.util import user_selection


class AsanaWrapper:
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
                " assignee, assignee_status, parent, notes"
            },
        )
        return tasks

    def generate_tasks_per_project(self) -> Iterator:
        workspace_id = self.select_workspace()
        projects = self.get_projects(workspace_id)
        for project in projects:
            tasks = self.get_tasks(project["id"])
            yield project, tasks
