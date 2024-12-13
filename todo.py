# A simple To-Do List Manager with intentionally introduced vulnerabilities

tasks = []

def add_task(task):
    """Add a new task to the list."""
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def view_tasks():
    """View all tasks in the list."""
    if not tasks:
        print("No tasks available. Add a new task!")
    else:
        print("Your tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def delete_task(task_number):
    """Delete a task by its number."""
    try:
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task}' removed successfully!")
    except IndexError:
        print("Invalid task number. Please try again.")

# Introduced vulnerability: Execute arbitrary code from input (Insecure)
def run_task(task_name):
    """Run a task. WARNING: This is insecure!"""
    print(f"Running task: {task_name}")
    exec(task_name)  # Using exec() introduces a vulnerability

def main():
    """Main function to run the To-Do List Manager."""
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Run Arbitrary Task (Insecure)")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            try:
                task_number = int(input("Enter the task number to delete: "))
                delete_task(task_number)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "4":
            task_name = input("Enter a Python command to run: ")
            run_task(task_name)  # Dangerous execution
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
