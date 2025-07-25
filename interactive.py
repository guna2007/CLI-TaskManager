#!/usr/bin/env python3
"""
Interactive Task Manager
A menu-driven interface for the task manager
"""

from task import TaskManager, Task


class InteractiveTaskManager:
    def __init__(self):
        self.task_manager = TaskManager()

    def display_menu(self):
        """Display the main menu"""
        print("\n" + "="*50)
        print("           CLI TASK MANAGER")
        print("="*50)
        print("1. Add Task")
        print("2. List All Tasks")
        print("3. List Pending Tasks")
        print("4. List Completed Tasks")
        print("5. Mark Task as Done")
        print("6. Mark Task as Pending")
        print("7. Update Task")
        print("8. Remove Task")
        print("9. Show Task Details")
        print("0. Exit")
        print("="*50)

    def display_tasks(self, tasks, title="Tasks"):
        """Display tasks in a formatted way"""
        if not tasks:
            print(f"\nNo {title.lower()} found.")
            return
        
        print(f"\n{title}:")
        print("-" * 60)
        for task_data in tasks:
            task = Task.from_dict(task_data)
            print(task)
        print("-" * 60)

    def add_task(self):
        """Add a new task interactively"""
        print("\n--- Add New Task ---")
        title = input("Enter task title: ").strip()
        if not title:
            print("Title cannot be empty!")
            return

        description = input("Enter task description (optional): ").strip()
        if not description:
            description = "Task to be done"

        while True:
            try:
                priority = input("Enter priority (1-10, default 5): ").strip()
                if not priority:
                    priority = 5
                else:
                    priority = int(priority)
                    if priority < 1 or priority > 10:
                        print("Priority must be between 1 and 10!")
                        continue
                break
            except ValueError:
                print("Please enter a valid number!")

        task = self.task_manager.add_task(title, description, priority)
        print(f"\n✓ Task added successfully: {task}")

    def mark_task_done(self):
        """Mark a task as done"""
        self.display_tasks(self.task_manager.list_tasks(status="pending"), "Pending Tasks")
        
        try:
            task_id = int(input("\nEnter task ID to mark as done: "))
            if self.task_manager.mark_done(task_id):
                print(f"✓ Task {task_id} marked as done")
            else:
                print(f"✗ Task {task_id} not found")
        except ValueError:
            print("Please enter a valid task ID!")

    def mark_task_pending(self):
        """Mark a task as pending"""
        self.display_tasks(self.task_manager.list_tasks(status="done"), "Completed Tasks")
        
        try:
            task_id = int(input("\nEnter task ID to mark as pending: "))
            if self.task_manager.mark_pending(task_id):
                print(f"✓ Task {task_id} marked as pending")
            else:
                print(f"✗ Task {task_id} not found")
        except ValueError:
            print("Please enter a valid task ID!")

    def update_task(self):
        """Update a task"""
        self.display_tasks(self.task_manager.list_tasks(), "All Tasks")
        
        try:
            task_id = int(input("\nEnter task ID to update: "))
            task = self.task_manager.get_task(task_id)
            if not task:
                print(f"✗ Task {task_id} not found")
                return

            print(f"\nCurrent task: {Task.from_dict(task)}")
            print("Leave empty to keep current value:")
            
            new_title = input(f"New title (current: {task['title']}): ").strip()
            new_description = input(f"New description (current: {task['description']}): ").strip()
            
            new_priority = None
            priority_input = input(f"New priority (current: {task['priority']}): ").strip()
            if priority_input:
                try:
                    new_priority = int(priority_input)
                    if new_priority < 1 or new_priority > 10:
                        print("Priority must be between 1 and 10! Keeping current value.")
                        new_priority = None
                except ValueError:
                    print("Invalid priority! Keeping current value.")
                    new_priority = None

            # Only update if values were provided
            title = new_title if new_title else None
            description = new_description if new_description else None

            if self.task_manager.update_task(task_id, title, description, new_priority):
                print(f"✓ Task {task_id} updated successfully")
                updated_task = self.task_manager.get_task(task_id)
                print(f"Updated task: {Task.from_dict(updated_task)}")
            else:
                print(f"✗ Failed to update task {task_id}")

        except ValueError:
            print("Please enter a valid task ID!")

    def remove_task(self):
        """Remove a task"""
        self.display_tasks(self.task_manager.list_tasks(), "All Tasks")
        
        try:
            task_id = int(input("\nEnter task ID to remove: "))
            task = self.task_manager.get_task(task_id)
            if task:
                confirm = input(f"Are you sure you want to remove '{task['title']}'? (y/N): ").strip().lower()
                if confirm == 'y':
                    self.task_manager.remove_task(task_id)
                    print(f"✓ Task {task_id} removed successfully")
                else:
                    print("Task removal cancelled")
            else:
                print(f"✗ Task {task_id} not found")
        except ValueError:
            print("Please enter a valid task ID!")

    def show_task_details(self):
        """Show detailed information about a task"""
        self.display_tasks(self.task_manager.list_tasks(), "All Tasks")
        
        try:
            task_id = int(input("\nEnter task ID to view details: "))
            task = self.task_manager.get_task(task_id)
            if task:
                print(f"\n--- Task Details ---")
                print(f"ID: {task['id']}")
                print(f"Title: {task['title']}")
                print(f"Description: {task['description']}")
                print(f"Priority: {task['priority']}/10")
                print(f"Status: {task['status']}")
                print(f"Created: {task.get('created_at', 'Unknown')}")
                if "completed_at" in task:
                    print(f"Completed: {task['completed_at']}")
            else:
                print(f"✗ Task {task_id} not found")
        except ValueError:
            print("Please enter a valid task ID!")

    def run(self):
        """Run the interactive task manager"""
        print("Welcome to CLI Task Manager!")
        
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (0-9): ").strip()

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.display_tasks(self.task_manager.list_tasks(), "All Tasks")
            elif choice == "3":
                self.display_tasks(self.task_manager.list_tasks(status="pending"), "Pending Tasks")
            elif choice == "4":
                self.display_tasks(self.task_manager.list_tasks(status="done"), "Completed Tasks")
            elif choice == "5":
                self.mark_task_done()
            elif choice == "6":
                self.mark_task_pending()
            elif choice == "7":
                self.update_task()
            elif choice == "8":
                self.remove_task()
            elif choice == "9":
                self.show_task_details()
            elif choice == "0":
                print("\nThank you for using CLI Task Manager!")
                break
            else:
                print("\nInvalid choice! Please enter a number between 0-9.")

            input("\nPress Enter to continue...")


if __name__ == "__main__":
    app = InteractiveTaskManager()
    app.run()