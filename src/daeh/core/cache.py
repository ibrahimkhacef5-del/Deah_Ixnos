from pathlib import Path
from daeh.core.config import CACHE_DIR

def get_cache_path(name: str, version: str) -> Path:
    return CACHE_DIR / f"{name}-{version}.tar.gz"

def is_cached(name: str, version: str) -> bool:
    return get_cache_path(name, version).exists()
