"""Student Task Manager - core task logic."""


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