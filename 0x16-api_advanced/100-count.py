#!/usr/bin/python3
"""getting the subs"""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """Printing counts of given words in hot posts."""
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
    try:
        results = res.json()
        if res.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        title = c.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                hot_times = len([t for t in title if t == word.lower()])
                if instances.get(word) is None:
                    instances[word] = hot_times
                else:
                    instances[word] += hot_times

    if after is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)

