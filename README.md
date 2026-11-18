# student-task-manager

A small Python console application for managing student tasks.

Project status: In Development

## Features
- Add tasks (empty titles are rejected)
- Display all tasks with their completion status
- Mark a task as completed
- Delete a task by its id
- Tasks are saved to `tasks.json` between runs

## Setup
1. Install Python 3.10 or newer.
2. Clone the repository:
   `git clone https://github.com/TahaAmerr/student-task-manager.git`
3. Open the folder: `cd student-task-manager`

No extra packages are needed.

## Usage
Run `python main.py` and choose an option from the menu (1-5).
See [docs/user-guide.md](docs/user-guide.md) for a walkthrough.

## Running the tests
`python -m unittest discover -s tests -v`

The same command runs automatically on GitHub Actions for every push to
`main` and every pull request to `main`.

## License
MIT - see the LICENSE file.
