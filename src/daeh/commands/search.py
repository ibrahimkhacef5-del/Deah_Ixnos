import click
from rich.console import Console
from rich.table import Table
from daeh.core.registry import load_registry
from daeh.utils.logger import info

console = Console()

@click.command()
@click.argument("query")
def search(query):
    """البحث عن حزمة"""
    registry = load_registry()
    packages = registry.get("packages", {})

    results = {
        name: data for name, data in packages.items()
        if query.lower() in name.lower()
    }

    if not results:
        info(f"لا نتائج لـ '{query}'")
        return

    table = Table(title=f"نتائج البحث: {query}")
    table.add_column("الاسم", style="cyan")
    table.add_column("الإصدار", style="magenta")
    table.add_column("الوصف", style="white")

    for name, data in results.items():
        table.add_row(name, data.get("version", "?"), data.get("description", ""))

    console.print(table)
