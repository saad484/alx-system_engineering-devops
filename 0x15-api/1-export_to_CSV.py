#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys


def export_to_csv(employee_id, username, tasks):
    filename = "{}.csv".format(employee_id)
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([employee_id, username,
                             task.get("completed"), task.get("title")])
    print("Data exported to {}".format(filename))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    try:
        user = requests.get(url + "users/{}".format(user_id)).json()
        username = user.get("username")
        todos = requests.get(url + "todos", params={"userId": user_id}).json()

        if "name" not in user:
            print("Employee not found.")
            sys.exit(1)

        completed_tasks = [
            {"completed": task["completed"], "title": task["title"]}
            for task in todos if task["completed"]
        ]

        print("Employee {} is done with tasks({}/{}):".format(
            username, len(completed_tasks), len(todos)))

        for task in completed_tasks:
            print("\t{}".format(task["title"]))

        export_to_csv(user_id, username, completed_tasks)

    except requests.RequestException as e:
        print("Error making API request:", e)
        sys.exit(1)
