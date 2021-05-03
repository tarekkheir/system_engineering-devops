#!/usr/bin/python3
""" script that returns information about his/her TODO list progress"""


import sys
import requests


def main():
    """ main function"""
    url = 'https://jsonplaceholder.typicode.com/users/'
    response = requests.get(url + sys.argv[1] + "/todos")
    json = response.json()

    total = len(json)
    tasks_done = 0

    tasks = []

    for task in json:
        if task.get('completed') is True:
            tasks.append(task.get('title'))
            tasks_done += 1

    r = requests.get(url + sys.argv[1])
    j = r.json()
    name = j['name']

    print("Employee {} is done with tasks({}/{}):"
          .format(name, tasks_done, total))

    for t in tasks:
        print("\t {}".format(t))


if __name__ == "__main__":
    main()
