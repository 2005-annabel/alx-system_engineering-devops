#!/usr/bin/python3
"""function that prints posts"""
import requests

def top_ten(subreddit):
    """printing titles of 10 hot posts"""
    hot_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    header = {
        "User-Agent": "alx:lin.api.adv:v1.0.0 (by /u/gena)"
    }
    param = {
        "limit": 10
    }
    response = requests.get(hot_url, headers=header, params=param,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
