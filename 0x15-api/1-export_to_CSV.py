#!/usr/bin/python3
"""
    Python script to export data in the CSV format.
    Records all tasks that are owned by an employee
"""

import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com"
    user = requests.get(f"{url}/users/{user_id}").json()
    todos = requests.get(f"{url}/todos",
                         params={"userId": user_id}).json()
    user_name = user.get('username')
    file_name = f"{user_id}.csv"

    with open(file_name, 'w', newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for task in todos:
            writer.writerow([user_id, user_name,
                            task.get('completed'),
                            task.get('title')])
