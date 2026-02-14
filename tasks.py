# tasks.py
# Simple command-line Task List for beginners

import json
import sys


FILE_NAME = "tasks.json"  # the file that will store tasks


def load_tasks():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=2)


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    for t in tasks:
        status = "Done" if t.get("done") else "Not Done"
        print(f'{t.get("id")}. {t.get("title")} - {status}')


def add_task(title):
    tasks = load_tasks()
    next_id = max((t.get("id", 0) for t in tasks), default=0) + 1
    tasks.append({"id": next_id, "title": title, "done": False})
    save_tasks(tasks)
    print("Task added.")


def mark_done(task_id):
    tasks = load_tasks()
    for t in tasks:
        if t.get("id") == task_id:
            t["done"] = True
            save_tasks(tasks)
            print("Task marked as done.")
            return

    print("Invalid task ID.")


def main():
    if len(sys.argv) < 2:
        print("Usage: py tasks.py [add/list/done] ...")
        return

    cmd = sys.argv[1]
    if cmd == "add" and len(sys.argv) >= 3:
        title = " ".join(sys.argv[2:])
        add_task(title)
    elif cmd == "list":
        list_tasks()
    elif cmd == "done" and len(sys.argv) == 3:
        try:
            mark_done(int(sys.argv[2]))
        except ValueError:
            print("Task ID must be a number.")
    else:
        print("Invalid command or arguments.")


if __name__ == "__main__":
    main()

