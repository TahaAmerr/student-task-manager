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