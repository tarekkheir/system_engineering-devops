#!/usr/bin/python3
""" task 0"""

import requests


def number_of_subscribers(subreddit):
    """ return number of subscribers of reddit programming"""
    url = "https://www.reddit.com/r/" + subreddit + "/about/.json"
    content = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64;'
    'rv:88.0) Gecko/20100101 Firefox/88.0'
    header = {'User-Agent': content}
    response = requests.get(url, headers=header)
    if response.status_code == 404:
        return 0

    json = response.json()
    if 'subscribers' in json['data']:
        data = json['data']['subscribers']
        return data
    return 0
