"""Student Task Manager - core task logic."""

import json
import os

DATA_FILE = "tasks.json"


def load_tasks(path=DATA_FILE):
    """Load tasks from a JSON file. Return an empty list if none exists."""
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_tasks(tasks, path=DATA_FILE):
    """Save the task list to a JSON file."""
    with open(path, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def add_task(tasks, title):
    """Add a new task with the given title and return it."""
    next_id = max((task["id"] for task in tasks), default=0) + 1
    task = {
        "id": next_id,
        "title": title,
        "completed": False,
    }
    tasks.append(task)
    return task

    
def display_tasks(tasks):
    """Print all tasks, or a message if there are none."""
    if not tasks:
        print("No tasks yet.")
        return
    for task in tasks:
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{task['id']}. {status} {task['title']}")

        
def complete_task(tasks, task_id):
    """Mark the task with the given id as completed. Return True if found."""
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return True
    return False


def delete_task(tasks, task_id):
    """Remove the task with the given id. Return True if found."""
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return True
    return False