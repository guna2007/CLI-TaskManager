import typer
from rich.console import Console 
from rich.table import Table

console = Console()
app = typer.Typer()

@app.command(short_help="adds a task")
def add(task: str, category: str):
    typer.echo(f"adding {task} , {category}")
    show()

@app.command(short_help="deletes a task")
def delete(id: int):
    typer.echo(f"deleting {id}")
    show()

@app.command(short_help="update a task")
def update(id: int):
    typer.echo(f"deleting {id}")
    show()
 
@app.command(short_help="markdone a task")
def complete(id: int):
    typer.echo(f"complete {id}")
    show()

@app.command(short_help="show all tasks")
def show():
    tasks = [
        {"id": 1, "task": "task1", "category": "work", "completed": False},
        {"id": 2, "task": "task2", "category": "office", "completed": True}
    ]

    console.print("[bold magenta]\nCLI TaskManager[/bold magenta]\n")

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("ID", style="dim", width=6)
    table.add_column("Task", min_width=20)
    table.add_column("Category", min_width=12, justify="right")
    table.add_column("Completed", min_width=12, justify="center")

    for t in tasks:
        status = "✅" if t["completed"] else "❌"
        table.add_row(str(t["id"]), t["task"], t["category"], status)

    console.print(table)
 
 
if __name__ == "__main__":
    app()
