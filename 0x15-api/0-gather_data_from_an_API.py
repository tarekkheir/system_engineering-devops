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

    for i in range(0, total):
        if json[i]['completed'] is True:
            tasks.append(json[i]['title'])
            tasks_done += 1

    r = requests.get(url + "2")
    j = r.json()
    name = j['name']

    print("Employee {} is done with tasks({}/{}):"
          .format(name, tasks_done, total))

    for t in tasks:
        print("\t {}".format(t))


if __name__ == "__main__":
    main()
