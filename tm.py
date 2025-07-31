import typer
from rich.console import Console 
from rich.table import Table

from tasks import Task
from data import save_tasks, load_tasks



console = Console()
app = typer.Typer()

@app.command(short_help="adds a task")
def add(task: str, category: str, date_due: str = None, id: int = None):
    tasks = load_tasks()

    if id is not None:
        if any(t.id == id for t in tasks):
            typer.echo(f"[!] Task with ID {id} already exists.")
            return
        
    args = []

    if date_due is not None:
         args.append(date_due)
    if id is not None:
         args.append(id)

    added_task = Task(task,category,*args)
    tasks.append(added_task)
    save_tasks(tasks)    

    typer.echo(f"[+] Added: {added_task.task} (ID: {added_task.id}, Started: {added_task.date_added}, Due: {added_task.date_due})")
    show()

@app.command(short_help="deletes a task")
def delete(id: int):
    tasks = load_tasks()
    tasks = [t for t in tasks if t.id != id]
    save_tasks(tasks)
    typer.echo(f"[-] Deleted task with ID {id}")
    show()

@app.command(short_help="update a task")
def update(id: int, task: str = None, category: str = None, date_due: str = None):
    tasks = load_tasks()
    for t in tasks:
        if t.id == id:
            if task: t.task = task
            if category: t.category = category
            if date_due: t.date_due = date_due
            typer.echo(f"[~] Updated task ID {id}")
            break
    else:
        typer.echo("[!] Task not found.")
    save_tasks(tasks)
    show()

 
@app.command(short_help="markdone a task")
def complete(id: int):
    tasks = load_tasks()
    for t in tasks:
        if t.id == id:
            t.mark_done()
            typer.echo(f"[✓] Marked task {id} as completed")
            break
    else:
        typer.echo("[!] Task not found.")
    save_tasks(tasks)
    show()

@app.command(short_help="Clears all tasks")
def clear():
    confirm = typer.confirm("Are you sure you want to delete ALL tasks?")
    if confirm:
        save_tasks([])
        typer.echo("✅ All tasks have been erased.")
    else:
        typer.echo("🚫 Deletion cancelled.")

@app.command(short_help="show all tasks")
def show():
    tasks = load_tasks()

    console.print("[bold magenta]\nCLI TaskManager[/bold magenta]\n")

    if not tasks:
        console.print("[italic]No tasks found.[/italic]")
        return

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("ID", style="dim", width=6)
    table.add_column("Task", min_width=20)
    table.add_column("Category", min_width=12, justify="right")
    table.add_column("Status", min_width=14, justify="center")
    table.add_column("Due", min_width=16, justify="center")

    for t in tasks:
        status = t.status_display()
        due = t.date_due if t.date_due else "--:--"
        table.add_row(str(t.id), t.task, t.category, status, due)

    console.print(table)
    console.print("\n")
 
 
if __name__ == "__main__":
    app()