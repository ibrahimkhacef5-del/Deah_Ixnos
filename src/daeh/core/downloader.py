import requests
from pathlib import Path
from daeh.core.cache import get_cache_path, is_cached
from daeh.core.registry import load_registry
from daeh.utils.errors import PackageNotFoundError

def download_package(name: str, version: str = "latest") -> Path:
    """تحميل حزمة C من المستودع"""
    if is_cached(name, version):
        return get_cache_path(name, version)

    registry = load_registry()
    packages = registry.get("packages", {})

    if name not in packages:
        raise PackageNotFoundError(f"الحزمة {name} غير موجودة")

    url = packages[name]["url"]
    response = requests.get(url, stream=True)

    if response.status_code == 404:
        raise PackageNotFoundError(f"الحزمة {name} غير موجودة في الرابط")

    response.raise_for_status()

    output = get_cache_path(name, version)
    with open(output, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    return output
