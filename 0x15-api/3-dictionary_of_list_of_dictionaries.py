#!/usr/bin/python3
""" script that returns information about his/her TODO list progress"""

import json
import requests


def main():
    """ main function"""
    url = 'https://jsonplaceholder.typicode.com/users/'
    response = requests.get(url)
    j = response.json()

    all_users_data = {}

    for user in j:
        r = requests.get(url + "/todos" + str(user['id'])).json()
        tasks = []

        for task in r:
            data = {"task": task['title'], "completed": task['completed'],
                    "username": user['username']}
            tasks.append(data)
        all_users_data[user['id']] = tasks

    with open("todo_all_employees.json", "w") as f:
        json.dump(all_users_data, f)


if __name__ == "__main__":
    main()
