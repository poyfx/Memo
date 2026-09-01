from datetime import datetime


def create_task(title):
    return {
        "title": title,
        "done": False,
        "create_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "complete_at": None,
    }


def mark_done(task):
    if task["done"]:
        return False

    task["done"] = True
    task["complete_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return True


def find_tasks(keyword, tasks):
    results = []
    for task in tasks:
        if keyword.lower() in task["title"].lower():
            results.append(task)
    return results


def update_task_title(task, new_title):
    if not new_title.strip():
        return False

    task["title"] = new_title.strip()
    return True


def remove_task(tasks, index):
    if index < 0 or index >= len(tasks):
        return None

    return tasks.pop(index)


def get_task_stats(tasks):
    total = len(tasks)
    completed = sum(1 for task in tasks if task["done"])
    pending = total - completed
    return total, completed, pending
