#!/usr/bin/env python3
"""
CLI Task Manager
A simple command-line task management application
"""

import argparse
import sys
from task import TaskManager, Task


def display_tasks(tasks, title="Tasks"):
    """Display tasks in a formatted way"""
    if not tasks:
        print(f"No {title.lower()} found.")
        return
    
    print(f"\n{title}:")
    print("-" * 50)
    for task_data in tasks:
        task = Task.from_dict(task_data)
        print(task)
    print("-" * 50)


def main():
    parser = argparse.ArgumentParser(description="CLI Task Manager")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add task command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task title")
    add_parser.add_argument("-d", "--description", default="Task to be done", help="Task description")
    add_parser.add_argument("-p", "--priority", type=int, default=5, choices=range(1, 11), help="Priority (1-10)")

    # List tasks command
    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument("-s", "--status", choices=["pending", "done"], help="Filter by status")
    list_parser.add_argument("-p", "--priority", type=int, choices=range(1, 11), help="Filter by priority")

    # Mark done command
    done_parser = subparsers.add_parser("done", help="Mark task as done")
    done_parser.add_argument("id", type=int, help="Task ID")

    # Mark pending command
    pending_parser = subparsers.add_parser("pending", help="Mark task as pending")
    pending_parser.add_argument("id", type=int, help="Task ID")

    # Remove task command
    remove_parser = subparsers.add_parser("remove", help="Remove a task")
    remove_parser.add_argument("id", type=int, help="Task ID")

    # Update task command
    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("id", type=int, help="Task ID")
    update_parser.add_argument("-t", "--title", help="New title")
    update_parser.add_argument("-d", "--description", help="New description")
    update_parser.add_argument("-p", "--priority", type=int, choices=range(1, 11), help="New priority (1-10)")

    # Show task command
    show_parser = subparsers.add_parser("show", help="Show a specific task")
    show_parser.add_argument("id", type=int, help="Task ID")

    # Clear all tasks command
    clear_parser = subparsers.add_parser("clear", help="Clear all tasks")
    clear_parser.add_argument("--confirm", action="store_true", help="Skip confirmation prompt")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    # Initialize task manager
    task_manager = TaskManager()

    # Handle commands
    if args.command == "add":
        task = task_manager.add_task(args.title, args.description, args.priority)
        print(f"✓ Task added: {task}")

    elif args.command == "list":
        if args.status:
            tasks = task_manager.list_tasks(status=args.status)
            display_tasks(tasks, f"{args.status.capitalize()} Tasks")
        elif args.priority:
            tasks = task_manager.list_by_priority(args.priority)
            display_tasks(tasks, f"Priority {args.priority} Tasks")
        else:
            tasks = task_manager.list_tasks()
            display_tasks(tasks, "All Tasks")

    elif args.command == "done":
        if task_manager.mark_done(args.id):
            print(f"✓ Task {args.id} marked as done")
        else:
            print(f"✗ Task {args.id} not found")

    elif args.command == "pending":
        if task_manager.mark_pending(args.id):
            print(f"✓ Task {args.id} marked as pending")
        else:
            print(f"✗ Task {args.id} not found")

    elif args.command == "remove":
        task = task_manager.get_task(args.id)
        if task:
            task_manager.remove_task(args.id)
            print(f"✓ Task {args.id} removed: {task['title']}")
        else:
            print(f"✗ Task {args.id} not found")

    elif args.command == "update":
        if task_manager.update_task(args.id, args.title, args.description, args.priority):
            print(f"✓ Task {args.id} updated")
            updated_task = task_manager.get_task(args.id)
            if updated_task:
                task_obj = Task.from_dict(updated_task)
                print(f"Updated task: {task_obj}")
        else:
            print(f"✗ Task {args.id} not found")

    elif args.command == "show":
        task = task_manager.get_task(args.id)
        if task:
            task_obj = Task.from_dict(task)
            print(f"\nTask Details:")
            print(f"ID: {task_obj.id}")
            print(f"Title: {task_obj.title}")
            print(f"Description: {task_obj.description}")
            print(f"Priority: {task_obj.priority}/10")
            print(f"Status: {task_obj.status}")
            print(f"Created: {task_obj.created_at}")
            if "completed_at" in task:
                print(f"Completed: {task['completed_at']}")
        else:
            print(f"✗ Task {args.id} not found")

    elif args.command == "clear":
        all_tasks = task_manager.list_tasks()
        if not all_tasks:
            print("No tasks to clear.")
        else:
            if args.confirm:
                task_manager.clear_all_tasks()
                print(f"✓ All {len(all_tasks)} task(s) cleared!")
            else:
                print(f"You have {len(all_tasks)} task(s).")
                confirm = input("Are you sure you want to delete ALL tasks? This cannot be undone! (type 'DELETE' to confirm): ").strip()
                if confirm == "DELETE":
                    task_manager.clear_all_tasks()
                    print("✓ All tasks have been cleared!")
                else:
                    print("Task clearing cancelled.")


if __name__ == "__main__":
    main()