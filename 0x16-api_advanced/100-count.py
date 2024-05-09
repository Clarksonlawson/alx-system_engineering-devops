#!/usr/bin/python3
"""
100-count
"""
import requests

def count_words(subreddit, word_list, after=None, word_count={}):
    """Recursively counts occurrences of keywords in hot articles for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}  # Custom User-Agent to avoid Too Many Requests error
    params = {"limit": 100, "after": after} if after else {"limit": 100}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json().get("data")
        if data:
            children = data.get("children")
            if children:
                for post in children:
                    title = post.get("data").get("title").lower()
                    for word in word_list:
                        if word.lower() in title.split():
                            word_count[word.lower()] = word_count.get(word.lower(), 0) + 1
                after = data.get("after")
                if after:
                    return count_words(subreddit, word_list, after, word_count)
                else:
                    sorted_counts = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
                    for word, count in sorted_counts:
                        print(f"{word}: {count}")
                    return
    elif response.status_code == 404:
        return  # Subreddit not found
    else:
        print("Request failed:", response.status_code)
        return

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = sys.argv[2].split()
        count_words(subreddit, word_list)

