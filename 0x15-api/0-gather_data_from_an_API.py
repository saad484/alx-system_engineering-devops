#!/usr/bin/python3

"""
Uses https://jsonplaceholder.typicode.com along with an employee ID to
return information about the employee's todo list progress
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    employee_id = int(argv[1])
    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = "{}users/{}".format(base_url, employee_id)
    todos_url = "{}todos?userId={}".format(base_url, employee_id)

    try:
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()

        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        completed_tasks = [task for task in todos_data if task['completed']]

        print("Employee {} is done with tasks({}/{}):".format(
            user_data['name'],
            len(completed_tasks),
            len(todos_data)
        ))

        for task in completed_tasks:
            print("\t{}".format(task['title']))

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        exit(1)
