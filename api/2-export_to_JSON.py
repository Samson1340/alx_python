import requests
import json
import sys

def get_employee_info(employee_id):
    # Endpoint for employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)

    if employee_response.status_code == 200:
        employee_data = employee_response.json()
        return employee_data['id'], employee_data['name']
    else:
        print(f"Error fetching employee details for ID {employee_id}")
        sys.exit(1)

def export_to_json(employee_id, tasks):
    # Define the JSON file name
    json_file_name = f"{employee_id}.json"

    # Write data to the JSON file
    with open(json_file_name, mode='w', encoding='utf-8') as json_file:
        json.dump({f"USER_ID": [{"task": task['title'], "completed": task['completed'], "username": task['username']} for task in tasks]}, json_file, indent=2)

    print(f"JSON file '{json_file_name}' has been created successfully.")

def get_todo_progress(employee_id):
    # Endpoint for employee's TODO list
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todo_response = requests.get(todo_url)

    if todo_response.status_code == 200:
        todo_data = todo_response.json()

        # Display employee TODO list progress
        user_id, username = get_employee_info(employee_id)
        print(f"Employee {username} is done with tasks ({len(todo_data)}/{len(todo_data)}):")

        # Display titles of completed tasks
        for task in todo_data:
            print(f"\t{task['title']}")

        # Export data to JSON
        export_to_json(user_id, todo_data)
    else:
        print(f"Error fetching TODO list for employee ID {employee_id}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python employee_todo_json.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_todo_progress(employee_id)
