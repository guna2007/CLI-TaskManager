# CLI Task Manager

A simple command-line task management application built with Python. Manage your tasks efficiently with both command-line arguments and interactive menu interfaces.

## Features

- ✅ Add, update, and remove tasks
- ✅ Mark tasks as done or pending
- ✅ List tasks with filtering options
- ✅ Priority system (1-10)
- ✅ Persistent storage in JSON format
- ✅ Two interfaces: CLI arguments and interactive menu
- ✅ Task details with timestamps

## Installation

1. Clone or download this repository
2. Ensure you have Python 3.6+ installed
3. No additional dependencies required (uses only standard library)

## Usage

### Command Line Interface

Use the CLI with command-line arguments for quick operations:

```bash
# Add a new task
python cli.py add "Complete project documentation" -d "Write comprehensive README and code comments" -p 8

# List all tasks
python cli.py list

# List only pending tasks
python cli.py list -s pending

# List only completed tasks
python cli.py list -s done

# List tasks by priority
python cli.py list -p 8

# Mark task as done
python cli.py done 1

# Mark task as pending
python cli.py pending 1

# Update a task
python cli.py update 1 -t "New title" -d "New description" -p 7

# Show task details
python cli.py show 1

# Remove a task
python cli.py remove 1
```

### Interactive Mode

For a menu-driven experience, run the interactive interface:

```bash
python interactive.py
```

This will present you with a menu where you can:

1. Add Task
2. List All Tasks
3. List Pending Tasks
4. List Completed Tasks
5. Mark Task as Done
6. Mark Task as Pending
7. Update Task
8. Remove Task
9. Show Task Details
10. Exit

## Task Properties

Each task has the following properties:

- **ID**: Unique identifier (auto-generated)
- **Title**: Task title (required)
- **Description**: Detailed description (optional, defaults to "Task to be done")
- **Priority**: Priority level from 1-10 (default: 5)
- **Status**: Either "pending" or "done"
- **Created At**: Timestamp when task was created
- **Completed At**: Timestamp when task was marked as done (if applicable)

## File Structure

```
cli_taskmanger/
├── task.py          # Core Task and TaskManager classes
├── cli.py           # Command-line interface
├── interactive.py   # Interactive menu interface
├── tasks.json       # Task storage (auto-created)
└── README.md        # This file
```

## Examples

### Adding Tasks with Different Priorities

```bash
# High priority task
python cli.py add "Fix critical bug" -d "Application crashes on startup" -p 10

# Medium priority task
python cli.py add "Update documentation" -p 5

# Low priority task
python cli.py add "Organize code files" -p 2
```

### Workflow Example

```bash
# Add some tasks
python cli.py add "Design database schema" -p 8
python cli.py add "Implement user authentication" -p 9
python cli.py add "Write unit tests" -p 7

# List all tasks
python cli.py list

# Mark first task as done
python cli.py done 1

# List only pending tasks
python cli.py list -s pending

# Update a task
python cli.py update 2 -d "Implement JWT-based authentication with refresh tokens"

# Show detailed view of a task
python cli.py show 2
```

## Data Storage

Tasks are stored in `tasks.json` in the following format:

```json
[
  {
    "id": 1,
    "title": "Complete project",
    "description": "Finish the CLI task manager",
    "priority": 8,
    "status": "pending",
    "created_at": "2024-01-15T10:30:00.123456"
  }
]
```

## Contributing

Feel free to fork this project and submit pull requests for improvements!

## License

This project is open source and available under the MIT License.
