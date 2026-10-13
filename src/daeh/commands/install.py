import click
from rich.console import Console
from daeh.core.downloader import download_package
from daeh.core.installer import install_c_package
from daeh.utils.logger import success, error, info

console = Console()

@click.command()
@click.argument("package_name")
@click.option("--version", default="latest", help="إصدار الحزمة")
def install(package_name, version):
    """تثبيت حزمة C جديدة"""
    info(f"جاري تثبيت {package_name} (الإصدار: {version})...")

    try:
        archive = download_package(package_name, version)
        manifest = install_c_package(archive)
        success(f"تم تثبيت {package_name} بنجاح")
        console.print(f"  [dim]الإصدار: {manifest.get('version')}[/dim]")
        console.print(f"  [dim]الترويسات في: ~/.daeh/include/[/dim]")
        console.print(f"  [dim]المكتبات في: ~/.daeh/lib/[/dim]")
    except Exception as e:
        error(f"فشل التثبيت: {e}")
