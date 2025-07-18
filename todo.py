import os

TASK_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    done, task = line.split("::", 1)
                    tasks.append({"task": task, "done": done == "1"})
    return tasks

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for t in tasks:
            done_flag = "1" if t["done"] else "0"
            file.write(f"{done_flag}::{t['task']}\n")

def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.\n")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "[✔]" if task["done"] else "[ ]"
            print(f"{i}. {status} {task['task']}")
        print()

def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append({"task": task, "done": False})
        save_tasks(tasks)
        print("Task added!\n")
    else:
        print("Cannot add empty task.\n")

def mark_task_done(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            save_tasks(tasks)
            print("Task marked as complete!\n")
        else:
            print("Invalid task number!.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Deleted task: {removed['task']}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    tasks = load_tasks()

    while True:
        print("------- To-Do List Manager-------")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as complete")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Choose one option (1-5): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice !. Please select between 1 and 5.\n")

if __name__ == "__main__":
    main()
