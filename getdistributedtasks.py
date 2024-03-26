import json
import os
import requests

def get_distributed_tasks_info(original_task_id, reltio_api_key, env, tenant_id):
    task_endpoint = f"{env}/reltio/{tenant_id}/tasks/{original_task_id}"
    headers = {
        "Authorization": f"Bearer {reltio_api_key}",
        "Content-Type": "application/json"
    }
    response = requests.get(task_endpoint, headers=headers)

    if response.status_code == 200:
        task_data = response.json()
        parallel_tasks_ids_str = task_data.get("parameters", {}).get("parallelTasksIds", "")
        parallel_tasks_ids = json.loads(parallel_tasks_ids_str)

        distributed_tasks_info = []

        for distributed_task_id in parallel_tasks_ids:
            distributed_task_info = get_task_info(distributed_task_id, reltio_api_key, env, tenant_id)
            if distributed_task_info:
                distributed_tasks_info.append(distributed_task_info)

        return distributed_tasks_info
    else:
        print("Failed to retrieve task information.")
        return None

def get_task_info(task_id, reltio_api_key, env, tenant_id):
    task_endpoint = f"{env}/reltio/{tenant_id}/tasks/{task_id}"
    headers = {
        "Authorization": f"Bearer {reltio_api_key}",
        "Content-Type": "application/json"
    }
    response = requests.get(task_endpoint, headers=headers)

    if response.status_code == 200:
        task_data = response.json()
        task_id = task_data.get("taskId")
        current_state = task_data.get("currentState")
        throughput = task_data.get("throughput")
        duration = task_data.get("duration")

        task_info = {
            "task_id": task_id,
            "currentState": current_state,
            "throughput": throughput,
            "duration": duration
        }
        return task_info
    else:
        print(f"Failed to retrieve information for task ID: {task_id}.")
        return None

# Prompt user for input
original_task_id = input("Enter the original task ID: ")
reltio_api_key = input("Enter your Reltio API key: ")
env = input("Enter the environment URL: ")
tenant_id = input("Enter your tenant ID: ")

# Prompt user to choose the directory to save the output file
output_directory = input("Enter the directory path to save the output file (leave blank for current directory): ").strip()
if not output_directory:
    output_directory = os.getcwd()

# Retrieve distributed tasks info
distributed_tasks_info = get_distributed_tasks_info(original_task_id, reltio_api_key, env, tenant_id)

# Save data to JSON file
if distributed_tasks_info:
    filename = input("Enter the filename to save the JSON data: ")
    if not filename.endswith('.json'):
        filename += '.json'
    output_path = os.path.join(output_directory, filename)
    print(f"Saving data to {output_path}")
    try:
        with open(output_path, 'w') as f:
            json.dump(distributed_tasks_info, f, indent=4)
        print(f"Data saved successfully!")
    except Exception as e:
        print(f"Error occurred while saving data: {e}")
