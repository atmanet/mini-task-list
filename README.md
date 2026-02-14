# Task List CLI

A simple **command-line Task List** program written in Python.  
This project allows you to **add, list, and mark tasks as done** using the terminal.

---

## **Features**

- Add new tasks with a title.
- List all tasks and see their status (Done / Not Done).
- Mark a task as completed.
- Saves tasks in a local `tasks.json` file.

---

## **Requirements**

- Python 3.13
- No external libraries required (uses built-in `json` and `sys` modules)

---

## **Usage**

Run the script from the terminal using:

```bash
py tasks.py add "Buy groceries"
py tasks.py list
py tasks.py done 1
