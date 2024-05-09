#!/usr/bin/python3
"""
1-top_ten
"""
import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}  # Custom User-Agent to avoid Too Many Requests error
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json().get("data")
        if data:
            children = data.get("children")
            if children:
                for post in children:
                    print(post.get("data").get("title"))
                return
    print("None")

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])

