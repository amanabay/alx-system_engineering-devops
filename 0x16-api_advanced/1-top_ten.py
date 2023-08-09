#!/usr/bin/python3
"""
    Script that queries Reddit api and prints titles of
    10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
        Queries the Reddit API and prints the titles of the
        first 10 hot posts listed for a given subreddit.

        Args:
            subreddit(str): Name of subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        for post in data["data"]["children"]:
            print(post["data"]["title"])
    else:
        print(None)
