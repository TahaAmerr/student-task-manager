"""Console interface for the Student Task Manager."""

from task_manager import (
    add_task, display_tasks, complete_task, delete_task,
    load_tasks, save_tasks,
)


def show_menu():
    print("\n=== Student Task Manager ===")
    print("1. Add task")
    print("2. Display tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")


def handle_add(tasks):
    title = input("Enter task title: ")
    try:
        add_task(tasks, title)
        print("Task added.")
    except ValueError as error:
        print(f"Error: {error}")


def handle_display(tasks):
    display_tasks(tasks)


def handle_complete(tasks):
    task_id = int(input("Enter task id to complete: "))
    if complete_task(tasks, task_id):
        print("Task marked as completed.")
    else:
        print("Task not found.")


def handle_delete(tasks):
    task_id = int(input("Enter task id to delete: "))
    if delete_task(tasks, task_id):
        print("Task deleted.")
    else:
        print("Task not found.")


def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            handle_add(tasks)
        elif choice == "2":
            handle_display(tasks)
        elif choice == "3":
            handle_complete(tasks)
        elif choice == "4":
            handle_delete(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()