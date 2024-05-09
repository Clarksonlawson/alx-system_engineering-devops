#!/usr/bin/python3
"""
2-recurse
"""
import requests

def recurse(subreddit, hot_list=[]):
    """Returns a list containing the titles of all hot articles for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}  # Custom User-Agent to avoid Too Many Requests error
    params = {"limit": 100}  # Increase limit to fetch more posts per request
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json().get("data")
        if data:
            children = data.get("children")
            if children:
                for post in children:
                    hot_list.append(post.get("data").get("title"))
                after = data.get("after")
                if after:
                    # Recursive call with the next page
                    return recurse(subreddit, hot_list, after=after)
                else:
                    return hot_list
    return None

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")

