#!/usr/bin/python3
import csv
import requests
import sys

if __name__ == "__main__":
    # Check if the user ID is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    
    try:
        # API endpoints
        user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
        todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
        
        # Fetch user data
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        
        user_data = user_response.json()
        username = user_data.get("username")
        
        # Fetch todos data
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        
        todos_data = todos_response.json()

        # CSV file name
        csv_file = f"{user_id}.csv"

        # Write to CSV
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            for task in todos_data:
                writer.writerow([user_id, username, str(task.get("completed")), task.get("title")])
        
        print(f"Data for user {user_id} has been written to {csv_file}.")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

