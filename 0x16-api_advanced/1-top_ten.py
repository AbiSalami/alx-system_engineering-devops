#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit. If not a valid subreddit, print None.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.
    If not a valid subreddit, prints None.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Custom"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            try:
                data = response.json().get("data", {})
                posts = data.get("children", [])
                for post in posts:
                    print(post.get("data", {}).get("title", None))
            except ValueError:
                print(None)
        else:
            print(None)
    except requests.RequestException:
        print(None)

