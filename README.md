# asana-pyexport
Export Asana projects and tasks in JSON.

# Example
## Export all your projects and tasks in JSON
Replace ```auth_token``` by your [Personal Access Token](https://asana.com/guide/help/api/api#gl-access-tokens) and ```save_file_path``` by the path of the file where you want to save the exported data.
```python
from asanapyexport.export import export_projects_and_tasks_to_json


auth_token = "replace by your token here"
save_file_path = "save/path/my-asana-data.json"
export_projects_and_tasks_to_json(auth_token, save_file_path, is_including_subtasks=True)
````

Result:
```json

[
        {
        "project": {
            "id": 1121238956815167,
            "gid": "1121238956815167",
            "archived": false,
            "created_at": "2019-05-05T19:03:16.536Z",
            "custom_fields": [],
            "members": [
                {
                    "id": 23423655671007,
                    "gid": "23423655671007",
                    "email": "potato@gmail.com",
                    "name": "Super Potato",
                    "photo": null,
                    "resource_type": "user",
                    "workspaces": [
                        {
                            "id": 23423655671012,
                            "gid": "23423655671012",
                            "name": "Terminator",
                            "resource_type": "workspace"
                        },
                        {
                            "id": 498346170860,
                            "gid": "498346170860",
                            "name": "Personal Projects",
                            "resource_type": "workspace"
                        }
                    ]
                }
            ],
            "modified_at": "2019-05-05T19:03:16.536Z",
            "name": "Saving the world",
            "notes": "",
            "owner": {
                "id": 23423655671007,
                "gid": "23423655671007",
                "email": "potato@gmail.com",
                "name": "Super Potato",
                "photo": null,
                "resource_type": "user",
                "workspaces": [
                    {
                        "id": 23423655671012,
                        "gid": "23423655671012",
                        "name": "Terminator",
                        "resource_type": "workspace"
                    },
                    {
                        "id": 498346170860,
                        "gid": "498346170860",
                        "name": "Personal Projects",
                        "resource_type": "workspace"
                    }
                ]
            },
            "resource_type": "project",
            "start_on": null
        },
        "tasks": [
            {
                "id": 1121238956815169,
                "gid": "1121238956815169",
                "assignee": {
                    "id": 23423655671007,
                    "gid": "23423655671007",
                    "email": "potato@gmail.com",
                    "name": "Super Potato",
                    "photo": null,
                    "resource_type": "user",
                    "workspaces": [
                        {
                            "id": 23423655671012,
                            "gid": "23423655671012",
                            "name": "Terminator",
                            "resource_type": "workspace"
                        },
                        {
                            "id": 498346170860,
                            "gid": "498346170860",
                            "name": "Personal Projects",
                            "resource_type": "workspace"
                        }
                    ]
                },
                "assignee_status": "inbox",
                "completed": true,
                "completed_at": "2019-05-05T19:04:36.338Z",
                "created_at": "2019-05-05T19:03:22.515Z",
                "dependencies": [],
                "due_on": "2019-05-31",
                "modified_at": "2019-05-05T19:04:36.464Z",
                "name": "Make a plan",
                "notes": "We need a plan to save the world.",
                "parent": null,
                "resource_type": "task",
                "sub_tasks": []
            },
            {
                "id": 1121238956815170,
                "gid": "1121238956815170",
                "assignee": null,
                "assignee_status": "upcoming",
                "completed": false,
                "completed_at": null,
                "created_at": "2019-05-05T19:03:31.332Z",
                "dependencies": [],
                "due_on": "2019-06-27",
                "modified_at": "2019-05-05T19:04:11.659Z",
                "name": "Save the world",
                "notes": "",
                "parent": null,
                "resource_type": "task",
                "sub_tasks": []
            },
            {
                "id": 1121238956815171,
                "gid": "1121238956815171",
                "assignee": null,
                "assignee_status": "upcoming",
                "completed": false,
                "completed_at": null,
                "created_at": "2019-05-05T19:03:39.483Z",
                "dependencies": [],
                "due_on": "2019-07-26",
                "modified_at": "2019-05-05T19:35:34.905Z",
                "name": "Celebrate",
                "notes": "",
                "parent": null,
                "resource_type": "task",
                "sub_tasks": [
                    {
                        "id": 1121238956815173,
                        "gid": "1121238956815173",
                        "assignee": null,
                        "assignee_status": "upcoming",
                        "completed": false,
                        "completed_at": null,
                        "created_at": "2019-05-05T19:04:55.079Z",
                        "due_on": null,
                        "modified_at": "2019-05-05T19:04:55.246Z",
                        "name": "invite guests",
                        "resource_type": "task"
                    },
                    {
                        "id": 1121238956815174,
                        "gid": "1121238956815174",
                        "assignee": null,
                        "assignee_status": "upcoming",
                        "completed": false,
                        "completed_at": null,
                        "created_at": "2019-05-05T19:05:02.263Z",
                        "due_on": null,
                        "modified_at": "2019-05-05T19:05:02.468Z",
                        "name": "find money",
                        "resource_type": "task"
                    },
                    {
                        "id": 1121238956815175,
                        "gid": "1121238956815175",
                        "assignee": null,
                        "assignee_status": "upcoming",
                        "completed": false,
                        "completed_at": null,
                        "created_at": "2019-05-05T19:05:07.105Z",
                        "due_on": null,
                        "modified_at": "2019-05-05T19:05:07.270Z",
                        "name": "buy stuff",
                        "resource_type": "task"
                    },
                    {
                        "id": 1121238956815176,
                        "gid": "1121238956815176",
                        "assignee": null,
                        "assignee_status": "upcoming",
                        "completed": false,
                        "completed_at": null,
                        "created_at": "2019-05-05T19:05:11.321Z",
                        "due_on": null,
                        "modified_at": "2019-05-05T19:05:11.479Z",
                        "name": "play with GPUs",
                        "resource_type": "task"
                    }
                ]
            }
        ]
    }
]
]
```


# Installation
Install [poetry](https://github.com/sdispater/poetry).
Then go at the root of this project and run:
```
make install
```
Or you can also run the command directly:
```
poetry install
```