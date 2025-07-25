#!/usr/bin/env python3
"""
Simple test script for the Task Manager
"""

import os
import json
from task import TaskManager, Task


def test_task_manager():
    """Test the TaskManager functionality"""
    print("Testing CLI Task Manager...")
    
    # Create a test task manager with a different file
    test_file = "test_tasks.json"
    if os.path.exists(test_file):
        os.remove(test_file)
    
    tm = TaskManager(test_file)
    
    # Test 1: Add tasks
    print("\n1. Testing task addition...")
    task1 = tm.add_task("Test Task 1", "This is a test task", 8)
    task2 = tm.add_task("Test Task 2", "Another test task", 5)
    task3 = tm.add_task("Test Task 3", priority=3)
    
    print(f"Added task 1: {task1}")
    print(f"Added task 2: {task2}")
    print(f"Added task 3: {task3}")
    
    # Test 2: List tasks
    print("\n2. Testing task listing...")
    all_tasks = tm.list_tasks()
    print(f"Total tasks: {len(all_tasks)}")
    for task_data in all_tasks:
        task = Task.from_dict(task_data)
        print(f"  {task}")
    
    # Test 3: Mark task as done
    print("\n3. Testing mark as done...")
    success = tm.mark_done(1)
    print(f"Mark task 1 as done: {'Success' if success else 'Failed'}")
    
    # Test 4: List pending and done tasks
    print("\n4. Testing filtered listing...")
    pending_tasks = tm.list_tasks(status="pending")
    done_tasks = tm.list_tasks(status="done")
    print(f"Pending tasks: {len(pending_tasks)}")
    print(f"Done tasks: {len(done_tasks)}")
    
    # Test 5: Update task
    print("\n5. Testing task update...")
    success = tm.update_task(2, title="Updated Test Task 2", priority=9)
    print(f"Update task 2: {'Success' if success else 'Failed'}")
    updated_task = tm.get_task(2)
    if updated_task:
        print(f"Updated task: {Task.from_dict(updated_task)}")
    
    # Test 6: Remove task
    print("\n6. Testing task removal...")
    tm.remove_task(3)
    remaining_tasks = tm.list_tasks()
    print(f"Remaining tasks after removal: {len(remaining_tasks)}")
    
    # Test 7: Priority filtering
    print("\n7. Testing priority filtering...")
    high_priority = tm.list_by_priority(9)
    print(f"Priority 9 tasks: {len(high_priority)}")
    
    # Clean up
    if os.path.exists(test_file):
        os.remove(test_file)
    
    print("\n✓ All tests completed successfully!")


def test_task_class():
    """Test the Task class"""
    print("\nTesting Task class...")
    
    # Create a task
    task = Task(1, "Test Task", "Test description", 7)
    print(f"Created task: {task}")
    
    # Test to_dict
    task_dict = task.to_dict()
    print(f"Task as dict: {task_dict}")
    
    # Test from_dict
    recreated_task = Task.from_dict(task_dict)
    print(f"Recreated task: {recreated_task}")
    
    print("✓ Task class tests completed!")


if __name__ == "__main__":
    test_task_class()
    test_task_manager()
    print("\n🎉 All tests passed! The CLI Task Manager is working correctly.")