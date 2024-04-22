#!/usr/bin/python3
"""
Module to gather data from an API.
"""

import requests
import sys


def get_employee_name(employee_id):
    """Function to get the employee's name from the API."""
    # Construct the URL for the API endpoint
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    # Send a GET request to the API endpoint
    try:
        response = requests.get(url)

        # Check if the request was successful
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

    # Extract the employee's name from the response
    employee_data = response.json()
    return employee_data.get('name')


def gather_data(employee_id):
    """Function to gather data from the API for a given employee ID."""
    # Get the employee's name
    employee_name = get_employee_name(employee_id)
    if employee_name is None:
        return

    # Construct the URL for the API endpoint
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Send a GET request to the API endpoint
    try:
        response = requests.get(url)

        # Check if the request was successful
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return

    # Extract relevant information from the response
    tasks_data = response.json()
    total_tasks = len(tasks_data)
    completed_tasks = [task['title'] for task in tasks_data if task['completed']]

    # Display the information in the specified format
    print(f"Employee {employee_name} is done with tasks ({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task}")


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    # Extract the employee ID from the command-line arguments
    employee_id = int(sys.argv[1])

    # Call the gather_data function with the provided employee ID
    gather_data(employee_id)

