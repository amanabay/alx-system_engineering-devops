#!/usr/bin/python3
"""
    Python script to export data in the JSON format.
    Records all tasks that are owned by an employee
"""

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get(f"{url}/users/").json()
    todos = requests.get(f"{url}/todos").json()

    file_name = "todo_all_employees.json"
    with open(file_name, 'w') as file:
        user_dict = {}
        for u in users:
            user_id = u.get("id")
            todos = requests.get(url + "todos",
                                 params={"userId": user_id}).json()
            tasks_list = []
            for task in todos:
                task_dict = {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": u.get("username")
                }
                tasks_list.append(task_dict)
        user_dict[user_id] = tasks_list

        json.dump(user_dict, file)
