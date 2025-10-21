import time
import json
import os
def greeting():
    print("""\nWelcome to this unique TO-DO LIST ! ! !\n""")
    time.sleep(2)
    print("Please enter the following details for better usability . . .\n")
    name = input("Your name: ")
    gender = input("Male (m) / Female (f): ")
    occ = input("Student (s) / Working (w): ")
    print(f"\nThank you {name.title()}! Let's get started\n")
    time.sleep(2)
def menu():
    time.sleep(2)
    print("\nWhich of the following things would you like to do ? ? ?\n")
    print("""1. Add a new task
2. Mark a task as done
3. Delete a task
4. View all tasks
5. Save tasks
6. Add due dates
7. Prioritize tasks
8. Categorize (work, study, personal, etc.)
9. Load tasks from file
10. Exit""")
    
def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)
    print("\nTasks saved successfully ! ! !\n")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found. Add one now!\n")
        return
    print("\n📜 YOUR TASKS:\n")
    for i, t in enumerate(tasks, 1):
        status = "Done . . ." if t["done"] else "Pending . . ."
        print(f"{i}. {t['task']} | {status}")
        if t.get("due_date"):
            print(f"Due: {t['due_date']}")
        if t.get("priority"):
            print(f"Priority: {t['priority']}")
        if t.get("category"):
            print(f"Category: {t['category']}")
        print("-" * 40)

def main():
    greeting()
    tasks = load_tasks()
    while True:
        menu()
        try:
            c = int(input("\nEnter your choice (1-10): "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        if c == 1:
            t = input("\nEnter the task: ")
            tasks.append({"task": t, "done": False})
            print("Task added ! ! !")
        elif c == 2:
            view_tasks(tasks)
            t = input("\nEnter the task name to mark as DONE: ")
            found = False
            for task in tasks:
                if task["task"].lower() == t.lower():
                    task["done"] = True
                    found = True
                    print("Task marked as done ! ! !")
                    break
            if not found:
                print("Task not found :(")
        elif c == 3:
            view_tasks(tasks)
            t = input("\nEnter the task name to DELETE: ")
            found = False
            for task in tasks:
                if task["task"].lower() == t.lower():
                    tasks.remove(task)
                    found = True
                    print("Task deleted ! ! !")
                    break
            if not found:
                print("Task not found :(")
        elif c == 4:
            view_tasks(tasks)
        elif c == 5:
            save_tasks(tasks)
        elif c == 6:
            view_tasks(tasks)
            t = input("\nEnter task name to add a due date: ")
            for task in tasks:
                if task["task"].lower() == t.lower():
                    task["due_date"] = input("Enter due date (e.g., 25-10-2025): ")
                    print("Due date added ! ! !")
                    break
            else:
                print("Task not found :(")
        elif c == 7:
            view_tasks(tasks)
            t = input("\nEnter task name to set priority: ")
            for task in tasks:
                if task["task"].lower() == t.lower():
                    task["priority"] = input("Enter priority (High/Medium/Low): ")
                    print("Priority set ! ! !")
                    break
            else:
                print("Task not found :(")
        elif c == 8:
            view_tasks(tasks)
            t = input("\nEnter task name to categorize: ")
            for task in tasks:
                if task["task"].lower() == t.lower():
                    task["category"] = input("Enter category (Work/Study/Personal): ")
                    print("Category added ! ! !")
                    break
            else:
                print("Task not found :(")
        elif c == 9:
            tasks = load_tasks()
            print("\n📂 Tasks loaded successfully ! ! !")
        elif c == 10:
            save_tasks(tasks)
            print("\nThank you for using the TO-DO LIST ! ! !")
            break
        else:
            print("\nInvalid choice. Please try again.")
if __name__ == "__main__":
    main()
