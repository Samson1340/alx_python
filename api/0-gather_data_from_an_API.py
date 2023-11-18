#!/usr/bin/python3
"""
Checks student output for returning info from REST API
"""

import requests
import sys

def get_employee_info(employee_id):
    # Endpoint for employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)

    if employee_response.status_code == 200:
        employee_data = employee_response.json()
        return employee_data['name']
    else:
        print(f"Error fetching employee details for ID {employee_id}")
        sys.exit(1)

def get_todo_progress(employee_id):
    # Endpoint for employee's TODO list
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todo_response = requests.get(todo_url)

    if todo_response.status_code == 200:
        todo_data = todo_response.json()

        # Count completed and total tasks
        completed_tasks = [task for task in todo_data if task['completed']]
        total_tasks = len(todo_data)

        # Display employee TODO list progress
        employee_name = get_employee_info(employee_id)
        print(f"Employee {employee_name} is done with tasks ({len(completed_tasks)}/{total_tasks}):")

        # Display titles of completed tasks
        for task in completed_tasks:
            print(f"\t{task['title']}")
    else:
        print(f"Error fetching TODO list for employee ID {employee_id}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python employee_todo.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_todo_progress(employee_id)
