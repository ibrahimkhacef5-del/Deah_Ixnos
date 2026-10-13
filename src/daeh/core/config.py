from pathlib import Path
import json

DAEH_HOME = Path.home() / ".daeh"
PACKAGES_DIR = DAEH_HOME / "packages"
CACHE_DIR = DAEH_HOME / "cache"
INCLUDE_DIR = DAEH_HOME / "include"
LIB_DIR = DAEH_HOME / "lib"
CONFIG_FILE = DAEH_HOME / "config.json"
INSTALLED_FILE = DAEH_HOME / "installed.json"
REGISTRY_FILE = DAEH_HOME / "registry.json"

def init_dirs():
    for d in [DAEH_HOME, PACKAGES_DIR, CACHE_DIR, INCLUDE_DIR, LIB_DIR]:
        d.mkdir(parents=True, exist_ok=True)

def load_config():
    if CONFIG_FILE.exists():
        return json.loads(CONFIG_FILE.read_text())
    return {
        "registry_url": "https://raw.githubusercontent.com/your-username/daeh-packages/main/registry.json"
    }

def save_config(config):
    CONFIG_FILE.write_text(json.dumps(config, indent=2))
