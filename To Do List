
tasks = []
def display_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added to your to-do list.")
def remove_task(index):
    if 1 <= index <= len(tasks):
        task = tasks.pop(index - 1)
        print(f"Task '{task}' removed from your to-do list.")
    else:
        print("Invalid task number.")
def main(): 
    print("Welcome to the To-Do List App!")
    while True:
        print("\n1. Display to-do list\n2. Add a task\n3. Remove a task\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            display_tasks()
        elif choice == '2':
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == '3':
            index = int(input("Enter the task number to remove: "))
            remove_task(index)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
