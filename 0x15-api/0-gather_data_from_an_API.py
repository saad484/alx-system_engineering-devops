#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    sessionReq = requests.Session()
#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress
and export data in the JSON format.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    sessionReq = requests.Session()

    idEmp = argv[1]
    idURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(idEmp)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(idEmp)

    employee = sessionReq.get(idURL)
    employeeName = sessionReq.get(nameURL)

    json_req = employee.json()
    usr = employeeName.json()['username']

    totalTasks = []
    updateUser = {}

    for all_Emp in json_req:
        totalTasks.append(
            {
                "task": all_Emp.get('title'),
                "completed": all_Emp.get('completed'),
                "username": usr,
            })
    updateUser[idEmp] = totalTasks

    file_Json = idEmp + ".json"
    with open(file_Json, 'w') as f:
        json.dump(updateUser, f)#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress
and export data in the JSON format.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    sessionReq = requests.Session()

    idEmp = argv[1]
    idURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(idEmp)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(idEmp)

    employee = sessionReq.get(idURL)
    employeeName = sessionReq.get(nameURL)

    json_req = employee.json()
    usr = employeeName.json()['username']

    totalTasks = []
    updateUser = {}

    for all_Emp in json_req:
        totalTasks.append(
            {
                "task": all_Emp.get('title'),
                "completed": all_Emp.get('completed'),
                "username": usr,
            })
    updateUser[idEmp] = totalTasks

    file_Json = idEmp + ".json"
    with open(file_Json, 'w') as f:
        json.dump(updateUser, f)
    idEmp = argv[1]
    idURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(idEmp)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(idEmp)

    employee = sessionReq.get(idURL)
    employeeName = sessionReq.get(nameURL)

    json_req = employee.json()
    name = employeeName.json()['name']

    totalTasks = 0

    for done_tasks in json_req:
        if done_tasks['completed']:
            totalTasks += 1

    print("Employee {} is done with tasks({}/{}):".
          format(name, totalTasks, len(json_req)))

    for done_tasks in json_req:
        if done_tasks['completed']:
            print("\t " + done_tasks.get('title'))
