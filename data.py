import json
import os
from tasks import Task

def save_tasks(tasks, filename="data.json"):
    with open(filename,"w") as f:
        json.dump([task.to_dict() for task in tasks],f, indent = 2)

def load_tasks(filename="data.json"):
    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        Task.id_count = 1
        return []

    with open(filename, "r") as f:
        data = json.load(f)
        tasks = [Task.from_dict(eachdict) for eachdict in data]
        if tasks:
            Task.id_count = max(t.id for t in tasks) + 1
        return tasks
