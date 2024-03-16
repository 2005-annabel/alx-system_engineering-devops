#!/usr/bin/python3
"""function that queries a list of all hot posts"""
import requests

def recurse(subreddit, hot_list=[], after="", count=0):
    """list of titles of all hot posts"""
    hot_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    header = {
        "User-Agent": "alx:lin.api.adv:v1.0.0 (by /u/gena)"
    }
    param_list = {
        "after": after,
        "count": count,
        "limit": 100
    }
    res = requests.get(hot_url, headers=header, params=param_list,
                            allow_redirects=False)
    if res.status_code == 404:
        return None

    results = res.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
