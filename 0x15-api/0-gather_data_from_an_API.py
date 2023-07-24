#!/usr/bin/python3
"""
    Script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com"
    user = requests.get(f"{url}/users/{employee_id}").json()
    todos = requests.get(f"{url}/todos/",
                         params={"userId": employee_id}).json()

    completed_tasks = [task.get('title') for task in todos
                       if task.get('completed') is True]

    name = user.get('name')
    done_tasks = len(completed_tasks)
    total_tasks = len(todos)

    print(f"Employee {name} is done with tasks({done_tasks}/{total_tasks})")

    for tasks in completed_tasks:
        print(f"\t {tasks}")
