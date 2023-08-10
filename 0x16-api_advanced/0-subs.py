#!/usr/bin/python3
"""
    Script that gives the number of subscribers
    for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
        Returns the number of subscribers for a given subreddit

        Args:
            subreddit(str): Name of subreddit
    """
    if subreddit is None or type(subreddit) is not str:
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    response = requests.get(url, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json()

            subscribers = data["data"]["subscribers"]

            return subscribers
        except KeyError:
            return 0
    else:
        return 0
