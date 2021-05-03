#!/usr/bin/python3
""" script that returns information about his/her TODO list progress"""


import sys
import requests
import csv


def main():
    """ main function"""
    url = 'https://jsonplaceholder.typicode.com/users/'
    response = requests.get(url + sys.argv[1] + "/todos")
    json = response.json()

    r = requests.get(url + sys.argv[1])
    j = r.json()
    name = j['username']

    with open("{}.csv".format(sys.argv[1]), "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        for task in json:
            row = [task.get('userId'), name, task.get('completed'), task.get('title')]
            writer.writerow(row)


if __name__ == "__main__":
    main()
