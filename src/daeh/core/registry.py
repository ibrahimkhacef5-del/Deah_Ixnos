import json
from daeh.core.config import REGISTRY_FILE, INSTALLED_FILE

def load_registry():
    if not REGISTRY_FILE.exists():
        return {"packages": {}}
    return json.loads(REGISTRY_FILE.read_text())

def save_registry(registry):
    REGISTRY_FILE.write_text(json.dumps(registry, indent=2))

def load_installed():
    if not INSTALLED_FILE.exists():
        return {}
    return json.loads(INSTALLED_FILE.read_text())

def save_installed(data):
    INSTALLED_FILE.write_text(json.dumps(data, indent=2))

def mark_installed(name, manifest):
    installed = load_installed()
    installed[name] = {
        "version": manifest.get("version", "?"),
        "type": manifest.get("type", "?"),
    }
    save_installed(installed)
