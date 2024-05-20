import json
import requests
from sys import argv


if __name__ == "__main__":
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Make a GET request to fetch all tasks
    response = requests.get(f"{base_url}/todos")
    tasks = response.json()

    # Organize tasks by user ID
    tasks_by_user = {}
    for task in tasks:
        user_id = task["userId"]
        task_details = {
            "username": task["title"],
            "task": task["title"],
            "completed": task["completed"]
        }

        if user_id in tasks_by_user:
            tasks_by_user[user_id].append(task_details)
        else:
            tasks_by_user[user_id] = [task_details]

    # Write the tasks to a JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(tasks_by_user, json_file)

