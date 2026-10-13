import click
import shutil
from pathlib import Path
from daeh.core.config import PACKAGES_DIR, INCLUDE_DIR, LIB_DIR
from daeh.utils.logger import success, error, info

@click.command()
@click.argument("package_name")
def remove(package_name):
    """حذف حزمة مثبتة"""
    info(f"جاري حذف {package_name}...")

    pkg_dir = PACKAGES_DIR / package_name
    if not pkg_dir.exists():
        error(f"الحزمة {package_name} غير مثبتة")
        return

    # حذف ملفات الترويسة
    for header in (INCLUDE_DIR).glob(f"{package_name}*.h"):
        header.unlink()

    # حذف المكتبات
    for lib in (LIB_DIR).glob(f"*{package_name}*"):
        lib.unlink()

    # حذف مجلد الحزمة
    shutil.rmtree(pkg_dir)

    success(f"تم حذف {package_name}")
