import datetime
class Task:

    id_count = 1
    def __init__(self, task, category, *args):
        self.task = task
        self.category = category
        self.date_added = None
        self.date_due = None
        self.completed = False

        str_count = 0
        manual_id = None

        for arg in args:
            if isinstance(arg, int):
                manual_id = arg
            elif isinstance(arg , str):
                if str_count == 0:
                    self.date_added = arg
                    str_count+=1
                elif str_count == 1:
                    self.date_due = arg
                    str_count+=1

        if manual_id is not None:
            self.id = manual_id
        else:
            self.id = Task.id_count
            Task.id_count+=1

        if self.date_added is None:
            self.date_added = datetime.datetime.now().strftime("%d/%m/%Y::%H:%M")

    def mark_done(self):
            self.completed = True
 
    def mark_undone(self):
            self.completed = False
 
    def is_overdue(self):
        if self.date_due in ("--:--", None) or self.completed:
            return False
        due = datetime.datetime.strptime(self.date_due, "%d/%m/%Y::%H:%M")
        return datetime.datetime.now() > due

    def status(self):
        if self.completed:
            return "✅ Done"
        elif self.is_overdue():
            return "🚨 Overdue"
        else:
            return "⏳ In Progress"

    def __str__(self):
        duedate = self.date_due if self.date_due is not None else "--:--"
        return (
            f"Status: {self.status()} |ID: {self.id} | Task: {self.task} | Category: {self.category} |Added: {self.date_added} | Due: {duedate}"
        )
    

 
task1 = Task("Learn Python", "Work","28/07/2025::15:00")
task2 = Task("Buy groceries", "Home", "28/07/2025::15:00", "29/07/2025::09:00", 101)
task3 = Task("Buy groceries", "Home", "28/07/2025::15:00", "29/07/2025::09:00")

task2.mark_done()

print(task1)
print(task2)
print(task3)
