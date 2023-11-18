import json
import requests


def export_to_json(all_tasks):
    # Define the JSON file name
    json_file_name = "todo_all_employees.json"

    # Write data to the JSON file
    with open(json_file_name, mode='w', encoding='utf-8') as json_file:
        json.dump(all_tasks, json_file, indent=2)

    print(f"JSON file '{json_file_name}' has been created successfully.")

def get_todo_progress():
    # Endpoint for all employees' TODO lists
    all_todo_url = "https://jsonplaceholder.typicode.com/todos"
    all_todo_response = requests.get(all_todo_url)

    if all_todo_response.status_code == 200:
        all_todo_data = all_todo_response.json()

        # Collect tasks for all employees
        all_tasks = {}
        for task in all_todo_data:
            user_id = task['userId']
            username = task['username']
            task_data = {"username": username, "task": task['title'], "completed": task['completed']}

            if user_id in all_tasks:
                all_tasks[user_id].append(task_data)
            else:
                all_tasks[user_id] = [task_data]

        # Export data to JSON
        export_to_json(all_tasks)
    else:
        print(f"Error fetching TODO lists for all employees")
        exit(1)

if __name__ == "__main__":
    get_todo_progress()
