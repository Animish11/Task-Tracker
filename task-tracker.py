"""
Task Tracker CLI
A command-line tool to manage tasks stored in a JSON file.
Run `python task-cli.py --help` for usage instructions.
"""

import argparse
import json
from datetime import datetime
import sys
import os

def load_tasks():
    """Load tasks from tasks.json. Create file if it doesn't exist."""
    if not os.path.exists('tasks.json'):
        return []
    try:
        with open('tasks.json', 'r') as f:
            tasks = json.load(f)
            # Ensure tasks is always a list, even if file is corrupted
            return tasks if isinstance(tasks, list) else []
    except json.JSONDecodeError:
        print("Error: tasks.json contains invalid JSON. Starting with empty list.")
        return []

def save_tasks(tasks):
    """Save tasks to tasks.json with indentation for readability."""
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=2)

def find_task_by_id(tasks, task_id):
    """Return task with matching ID or None if not found."""
    return next((task for task in tasks if task['id'] == task_id), None)

def get_next_id(tasks):
    """Generate the next unique task ID."""
    return max(task['id'] for task in tasks) + 1 if tasks else 1

def main():
    # Configure command-line argument parser
    parser = argparse.ArgumentParser(description='Manage your tasks via CLI')
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Add command: Create a new task
    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('description', type=str, help='Task description (enclose in quotes)')

    # Update command: Modify an existing task
    update_parser = subparsers.add_parser('update')
    update_parser.add_argument('id', type=int, help='Task ID to update')
    update_parser.add_argument('description', type=str, help='New task description')

    # Delete command: Remove a task
    delete_parser = subparsers.add_parser('delete')
    delete_parser.add_argument('id', type=int, help='Task ID to delete')

    # Status commands: Mark as in-progress/done
    mark_ip_parser = subparsers.add_parser('mark-in-progress')
    mark_ip_parser.add_argument('id', type=int, help='Task ID to mark as in-progress')
    mark_done_parser = subparsers.add_parser('mark-done')
    mark_done_parser.add_argument('id', type=int, help='Task ID to mark as done')

    # List command: Show tasks (optionally filtered by status)
    list_parser = subparsers.add_parser('list')
    list_parser.add_argument('status', nargs='?', default=None,
                            choices=['todo', 'in-progress', 'done'],
                            help='Filter by task status')

    args = parser.parse_args()
    tasks = load_tasks()

    # Handle 'add' command
    if args.command == 'add':
        description = args.description.strip()
        if not description:
            print("Error: Task description cannot be empty.")
            sys.exit(1)

        new_task = {
            'id': get_next_id(tasks),
            'description': description,
            'status': 'todo',
            'createdAt': datetime.now().isoformat(),
            'updatedAt': datetime.now().isoformat()
        }
        tasks.append(new_task)
        save_tasks(tasks)
        print(f'Task added successfully (ID: {new_task["id"]})')

    # Handle 'update' command
    elif args.command == 'update':
        task = find_task_by_id(tasks, args.id)
        if not task:
            print(f'Error: Task ID {args.id} does not exist.')
            sys.exit(1)

        new_description = args.description.strip()
        if not new_description:
            print("Error: New description cannot be empty.")
            sys.exit(1)

        task['description'] = new_description
        task['updatedAt'] = datetime.now().isoformat()
        save_tasks(tasks)
        print(f'Updated task ID {args.id}.')

    # Handle 'delete' command
    elif args.command == 'delete':
        initial_count = len(tasks)
        tasks = [task for task in tasks if task['id'] != args.id]
        if len(tasks) == initial_count:
            print(f'Error: Task ID {args.id} not found.')
            sys.exit(1)
        save_tasks(tasks)
        print(f'Deleted task ID {args.id}.')

    # Handle status changes
    elif args.command in ('mark-in-progress', 'mark-done'):
        task = find_task_by_id(tasks, args.id)
        if not task:
            print(f'Error: Task ID {args.id} not found.')
            sys.exit(1)

        new_status = 'in-progress' if args.command == 'mark-in-progress' else 'done'
        task['status'] = new_status
        task['updatedAt'] = datetime.now().isoformat()
        save_tasks(tasks)
        print(f'Task ID {args.id} marked as {new_status}.')

    # Handle 'list' command
    elif args.command == 'list':
        filtered_tasks = tasks
        if args.status:
            filtered_tasks = [t for t in tasks if t['status'] == args.status]

        if not filtered_tasks:
            print('No tasks found.')
            return

        for task in filtered_tasks:
            print(f"ID: {task['id']}")
            print(f"Description: {task['description']}")
            print(f"Status: {task['status']}")
            print(f"Created: {task['createdAt']}")
            print(f"Last Updated: {task['updatedAt']}")
            print('-' * 20)

if __name__ == '__main__':
    main()
