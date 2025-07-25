import json
import os
from datetime import datetime


class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Load tasks from JSON file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                return []
        return []

    def save_tasks(self):
        """Save tasks to JSON file"""
        with open(self.filename, "w") as f:
            json.dump(self.tasks, f, indent=2)

    def get_next_id(self):
        """Get the next available ID"""
        if not self.tasks:
            return 1
        return max(task["id"] for task in self.tasks) + 1

    def add_task(self, title, description="Task to be done", priority=5):
        """Add a new task"""
        task = Task(
            id=self.get_next_id(),
            title=title,
            description=description,
            priority=priority
        )
        self.tasks.append(task.to_dict())
        self.save_tasks()
        return task

    def remove_task(self, task_id):
        """Remove a task by ID"""
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        self.save_tasks()

    def mark_done(self, task_id):
        """Mark a task as done"""
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = "done"
                task["completed_at"] = datetime.now().isoformat()
                self.save_tasks()
                return True
        return False

    def mark_pending(self, task_id):
        """Mark a task as pending"""
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = "pending"
                if "completed_at" in task:
                    del task["completed_at"]
                self.save_tasks()
                return True
        return False

    def update_task(self, task_id, title=None, description=None, priority=None):
        """Update task details"""
        for task in self.tasks:
            if task["id"] == task_id:
                if title is not None:
                    task["title"] = title
                if description is not None:
                    task["description"] = description
                if priority is not None:
                    task["priority"] = priority
                self.save_tasks()
                return True
        return False

    def get_task(self, task_id):
        """Get a specific task by ID"""
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None

    def list_tasks(self, status=None):
        """List all tasks or filter by status"""
        if status:
            return [task for task in self.tasks if task["status"] == status]
        return self.tasks

    def list_by_priority(self, priority):
        """List tasks by priority level"""
        return [task for task in self.tasks if task["priority"] == priority]


class Task:
    def __init__(self, id, title, description="Task to be done", priority=5, status="pending"):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
        self.created_at = datetime.now().isoformat()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
            "created_at": self.created_at
        }

    def __str__(self):
        status_symbol = "✓" if self.status == "done" else "○"
        priority_stars = "★" * self.priority
        return f"[{self.id}] {status_symbol} {self.title} ({priority_stars}) - {self.description}"

    @classmethod
    def from_dict(cls, data):
        """Create Task instance from dictionary"""
        task = cls(
            id=data["id"],
            title=data["title"],
            description=data.get("description", "Task to be done"),
            priority=data.get("priority", 5),
            status=data.get("status", "pending")
        )
        if "created_at" in data:
            task.created_at = data["created_at"]
        return task
