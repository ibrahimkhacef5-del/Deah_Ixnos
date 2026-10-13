import json
import shutil
import tarfile
from pathlib import Path
from daeh.core.config import PACKAGES_DIR, INCLUDE_DIR, LIB_DIR
from daeh.core.registry import mark_installed
from daeh.utils.errors import InstallationError

def install_c_package(archive_path: Path) -> dict:
    """تثبيت حزمة C"""
    extract_dir = PACKAGES_DIR / archive_path.stem.replace(".tar", "")

    if extract_dir.exists():
        shutil.rmtree(extract_dir)
    extract_dir.mkdir(parents=True)

    with tarfile.open(archive_path, "r:gz") as tar:
        tar.extractall(path=extract_dir)

    manifest_path = extract_dir / "manifest.json"
    if not manifest_path.exists():
        raise InstallationError("manifest.json غير موجود في الحزمة")

    manifest = json.loads(manifest_path.read_text())
    pkg_name = manifest.get("name", extract_dir.name)

    INCLUDE_DIR.mkdir(exist_ok=True)
    for header in manifest.get("headers", []):
        src = extract_dir / header
        if src.exists():
            shutil.copy(src, INCLUDE_DIR / src.name)

    LIB_DIR.mkdir(exist_ok=True)
    for lib in manifest.get("libs", []):
        src = extract_dir / lib
        if src.exists():
            shutil.copy(src, LIB_DIR / src.name)

    mark_installed(pkg_name, manifest)
    return manifest
