#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.
"""

import requests
import sys

def get_employee_todo_list(employee_id):
    """Fetches the to-do list information for a given employee ID."""
    # Construct the URL for the API endpoints
    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = base_url + "users/{}".format(employee_id)
    todos_url = base_url + "todos"

    try:
        # Fetch user information
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()

        # Fetch user's to-do list
        todos_response = requests.get(todos_url, params={"userId": employee_id})
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        return user_data, todos_data
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None, None

def print_todo_list(user_data, todos_data):
    """Prints the to-do list information."""
    if user_data is None or todos_data is None:
        return

    # Extract relevant information
    user_name = user_data.get("name")
    completed_tasks = [t.get("title") for t in todos_data if t.get("completed") is True]
    total_tasks = len(todos_data)

    # Print information in the specified format
    print("Employee {} is done with tasks ({}/{}):".format(user_name, len(completed_tasks), total_tasks))
    for task in completed_tasks:
        print("\t{}".format(task))

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    # Extract the employee ID from the command-line arguments
    employee_id = int(sys.argv[1])

    # Fetch and print the to-do list information
    user_data, todos_data = get_employee_todo_list(employee_id)
    print_todo_list(user_data, todos_data)

