#!/usr/bin/python3

"""
A function that query the number of subscriber from reddit API
"""

import requests


def number_of_subscribers(susbreddit):
    """returns the numbers of subs"""
    url = "https://www.reddit.com/r/{}/about.json".format(susbreddit)
    headers = {
        "User-Agents": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"

    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
