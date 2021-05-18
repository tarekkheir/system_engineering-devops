#!/usr/bin/python3
""" task 2"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """ returns a list containing the titles of all
    hot articles for a given subreddit"""
    url = 'https://www.reddit.com/r/' + subreddit + '/hot/.json'
    content = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64;'
    'rv:88.0) Gecko/20100101 Firefox/88.0'
    header = {'User-Agent': content}
    response = requests.get(url, headers=header)

    if response.status_code == 404:
        return None
    else:
        after = response.json()['data']['after']
        children = response.json()['data']['children']
        for title in children:
            hot_list.append(title)
        if after is None:
            return hot_list

    return recurse(subreddit, hot_list, after)
