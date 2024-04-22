#!/usr/bin/python3
"""Fetches and prints to-do list information for a given employee ID."""

import requests
import sys

if __name__ == "__main__":
    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information from the API
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()

    # Fetch to-do list for the specified user ID from the API
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    # Filter completed tasks and count the total number of tasks
    completed = [t.get("title") for t in todos if t.get("completed") is True]
    total_tasks = len(todos)

    # Print the user's name, number of completed tasks, and total number of tasks
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), total_tasks))

    # Print completed tasks with proper indentation
    [print("\t{}".format(c)) for c in completed]

