#!/usr/bin/python3
"""
    Python script to export data in the JSON format.
    Records all tasks that are owned by an employee
"""

import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com"
    user = requests.get(f"{url}/users/{user_id}").json()
    todos = requests.get(f"{url}/todos/",
                         params={"userId": user_id}).json()
    user_name = user.get('username')
    file_name = f"{user_id}.json"

    with open(file_name, 'w') as file:
        json.dump({user_id:
                  [{"task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": user_name} for task in todos]}, file)
