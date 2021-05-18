#!/usr/bin/python3
""" task 1"""

import requests


def top_ten(subreddit):
    """ get top ten hot post of a specific subreddit"""
    url = 'https://www.reddit.com/r/' + subreddit + '/hot/.json?limit=10'
    content = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64;'
    'rv:88.0) Gecko/20100101 Firefox/88.0'
    header = {'User-Agent': content}
    response = requests.get(url, headers=header)
    if response.status_code == 404:
        return 0

    json = response.json()

    if 'children' in json['data']:
        children = json['data']['children']
        for child in children:
            print(child['data']['title'])

    return 0
