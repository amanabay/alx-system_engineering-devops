#!/usr/bin/python3
"""
    Python script to export data in the CSV format.
    Records all tasks that are owned by an employee
"""

import csv
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com"
    user = requests.get(f"{url}/users/{employee_id}").json()
    todos = requests.get(f"{url}/todos/",
                         params={"userId": employee_id}).json()
    user_name = user.get('username')
    file_name = f"{employee_id}.csv"

    with open(file_name, 'w', newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for task in todos:
            writer.writerow([employee_id, user_name,
                            task.get('completed'),
                            task.get('title')])
