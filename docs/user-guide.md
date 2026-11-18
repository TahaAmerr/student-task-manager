# User Guide

## Starting the app
Open a terminal in the project folder and run:

    python main.py

## Menu options
1. **Add task** - type a title and press Enter. Empty titles are rejected.
2. **Display tasks** - lists every task. `[ ]` means pending, `[x]` means completed.
3. **Complete task** - type the id number of the task to mark it as done.
4. **Delete task** - type the id number of the task to remove it.
5. **Exit** - saves your tasks to `tasks.json` and closes the app.

## Tips
- Task ids are shown at the start of each line when you display tasks.
- If you type a letter instead of a number for an id, the app will ask for a number.
- Your tasks are loaded again the next time you start the app.
