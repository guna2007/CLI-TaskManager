import datetime
from rich.text import Text
class Task:

    id_count = 1
    def __init__(self, task, category, *args):
        self.task = task
        self.category = str(category)
        self.date_added = datetime.datetime.now().strftime("%d/%m/%Y::%H:%M")
        self.date_due = None
        self.completed = False

        str_count = 0
        manual_id = None

        for arg in args:
            if isinstance(arg, int):
                manual_id = arg
            elif isinstance(arg , str):
                if str_count == 0:
                    self.date_due = arg
                    str_count+=1

                    

        if manual_id is not None:
            self.id = manual_id
        else:
            self.id = Task.id_count
            Task.id_count+=1

        

    def mark_done(self):
            self.completed = True
 
    def mark_undone(self):
            self.completed = False

    def is_overdue(self):
        try:
            due = datetime.datetime.strptime(self.date_due, "%d/%m/%Y::%H:%M")
            return datetime.datetime.now() > due if not self.completed else False
        except Exception:
            return False


    def status(self):
        if self.completed:
            return "✅ Done"
        elif self.is_overdue():
            return "🚨 Overdue"
        else:
            return "⏳ In Progress"
        
    def status_display(self):
        status_text = self.status()
        color_map = {
            "✅ Done": "green",
            "⏳ In Progress": "white",
            "🚨 Overdue": "red"
        }
        return Text(status_text, style=color_map.get(status_text, "yellow"))

    def __str__(self):
        duedate = self.date_due if self.date_due is not None else "--:--"
        return (
            f"[{self.status()}] Task #{self.id}: {self.task}\n"
            f"  • Category: {self.category}\n"
            f"  • Added: {self.date_added}\n"
            f"  • Due: {duedate}"
        )

    
    def to_dict(self):
        return(
            {
                "id": self.id,
                "task": self.task,
                "category": self.category,
                "date_added": self.date_added,
                "date_due": self.date_due,
                "completed": self.completed
            }
        )
    @classmethod
    def from_dict(cls,data):
        task = cls(
            data["task"],
            data["category"],
            data["date_due"],
            data["id"]
        )
        task.date_added = data["date_added"]
        task.completed = data["completed"]
        return task
        
    