# A simple To-Do List Manager in Python

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

def main():
    """Main function to run the To-Do List Manager."""
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            task_number = int(input("Enter the task number to delete: "))
            delete_task(task_number)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
