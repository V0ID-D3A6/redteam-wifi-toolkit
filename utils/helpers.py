import json
import os

def ensure_dir(path):
    if path:
        os.makedirs(path, exist_ok=True)

def save_json(path, data):
    ensure_dir(os.path.dirname(path))
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def load_json(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} not found")
    with open(path) as f:
        return json.load(f)
