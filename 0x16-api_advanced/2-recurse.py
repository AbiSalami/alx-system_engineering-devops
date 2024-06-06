#!/usr/bin/python3
"""
Function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit, return None.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, return None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Custom"}
    params = {"after": after, "limit": 100}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            try:
                data = response.json().get("data", {})
                after = data.get("after", None)
                posts = data.get("children", [])
                if not posts:
                    return hot_list if hot_list else None
                for post in posts:
                    hot_list.append(post.get("data", {}).get("title", None))
                if after:
                    return recurse(subreddit, hot_list, after)
                return hot_list
            except ValueError:
                return None
        else:
            return None
    except requests.RequestException:
        return None

