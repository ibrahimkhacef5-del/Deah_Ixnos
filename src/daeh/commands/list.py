import click
from rich.console import Console
from rich.table import Table
from daeh.core.registry import load_installed
from daeh.utils.logger import info

console = Console()

@click.command(name="list")
def list_packages():
    """عرض الحزم المثبتة"""
    installed = load_installed()

    if not installed:
        info("لا توجد حزم مثبتة")
        return

    table = Table(title="الحزم المثبتة")
    table.add_column("الاسم", style="cyan")
    table.add_column("الإصدار", style="magenta")
    table.add_column("النوع", style="green")

    for name, data in installed.items():
        table.add_row(name, data.get("version", "?"), data.get("type", "?"))

    console.print(table)
