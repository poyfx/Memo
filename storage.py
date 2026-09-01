import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "tasks.json"


def load_tasks():
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(tasks):
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(tasks, file, ensure_ascii=False, indent=2)
    except OSError:
        print("保存失败")
