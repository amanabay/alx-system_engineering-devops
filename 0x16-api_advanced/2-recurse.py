#!/usr/bin/python3
"""
    Script that queries the Reddit API and prints titles of
    hot posts listed for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[]):
    """
    Recursively queries the Reddit API and retrieves the titles of the
    first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): Name of the subreddit

    Returns:
        hot_list: List containing titles of hot posts,
                  or None if subreddit is invalid
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    response = requests.get(url, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        if len(posts) == 0:
            return hot_list

        for post in posts:
            hot_list.append(post["data"]["title"])

        after = data["data"]["after"]

        if after:
            return recurse(subreddit, hot_list=hot_list)
        else:
            return hot_list
    else:
        return None
