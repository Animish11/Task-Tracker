# Task-Tracker
Task Tracker CLI is a command-line tool to manage tasks (add/update/delete) and track statuses (todo). Stores data in JSON, supports status-based filtering, and handles errors. Built with Python’s native modules—no external libraries. Offers simple terminal commands for efficient to-do list management with timestamps and persistent storage

**Step-by-Step Explanation:**

1. **Final Testing:**
   - All commands (`add`, `update`, `delete`, `mark-in-progress`, `mark-done`, `list`) were tested for valid and invalid inputs.
   - Edge cases (e.g., empty descriptions, invalid task IDs) are gracefully handled with error messages.
   - The JSON file (`tasks.json`) is validated for correct data persistence.

2. **Code Cleanup:**
   - Added docstrings and comments to improve readability.
   - Ensured consistent error handling and exit codes.

3. **ReadMe Documentation:**
   - Created a user-friendly guide explaining installation, commands, and examples.

---

# Task Tracker CLI - ReadMe

A simple CLI to manage your tasks and to-do list. Track tasks as `todo`, `in-progress`, or `done`, and store them in a JSON file.

## Installation

1. **Prerequisites**: Python 3.6+ installed.
2. **Download**: Save the script as `task-cli.py`.

## Usage

Run commands in the terminal using `python task-cli.py [command] [arguments]`.

### Commands

| Command               | Description                                  | Example                                   |
|-----------------------|----------------------------------------------|-------------------------------------------|
| `add "Description"`   | Add a new task                               | `python task-cli.py add "Buy groceries"`  |
| `update ID "New Desc"`| Update a task’s description                 | `python task-cli.py update 1 "New task"`  |
| `delete ID`           | Delete a task                               | `python task-cli.py delete 1`             |
| `mark-in-progress ID` | Mark task as `in-progress`                  | `python task-cli.py mark-in-progress 1`   |
| `mark-done ID`        | Mark task as `done`                         | `python task-cli.py mark-done 1`          |
| `list [status]`       | List all tasks (or filter by `todo`/`in-progress`/`done`) | `python task-cli.py list done` |

### Examples

```bash
# Add a task
python task-cli.py add "Finish project report"

# Update task ID 1
python task-cli.py update 1 "Finish project report and submit"

# Mark task ID 1 as done
python task-cli.py mark-done 1

# List all in-progress tasks
python task-cli.py list in-progress
```

## Task Properties

Each task in `tasks.json` includes:
- `id`: Unique numeric ID.
- `description`: Task description.
- `status`: `todo`, `in-progress`, or `done`.
- `createdAt`: ISO timestamp of creation.
- `updatedAt`: ISO timestamp of last update.

## Error Handling
- Invalid commands/arguments show helpful error messages.
- Empty descriptions or non-existent task IDs are flagged.

---


This ReadMe and code provide a complete, user-friendly CLI task tracker that meets all requirements!
