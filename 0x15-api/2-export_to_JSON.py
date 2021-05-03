#!/usr/bin/python3
""" script that returns information about his/her TODO list progress"""

import json
import requests
import sys


def main():
    """ main function"""
    url = 'https://jsonplaceholder.typicode.com/users/'
    response = requests.get(url + sys.argv[1] + "/todos")
    j = response.json()

    r = requests.get(url + sys.argv[1])
    jr = r.json()
    name = jr['username']

    with open("{}.json".format(sys.argv[1]), "w") as f:
        tasks = []
        for task in j:
            data = {"task": task['title'], "completed": task['completed'],
                    "username": name}
            tasks.append(data)

        file_data = {sys.argv[1]: tasks}
        json.dump(file_data, f)


if __name__ == "__main__":
    main()
