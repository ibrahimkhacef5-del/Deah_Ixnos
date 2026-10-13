from rich.console import Console

console = Console()

def info(msg): console.print(f"[blue]ℹ[/blue] {msg}")
def success(msg): console.print(f"[green]✓[/green] {msg}")
def warning(msg): console.print(f"[yellow]⚠[/yellow] {msg}")
def error(msg): console.print(f"[red]✗[/red] {msg}")
