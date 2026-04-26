from manager import TaskManager

manager = TaskManager()

while True:
    print("\n1. Add task")
    print("2. Show tasks")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        title = input("Enter title: ")
        deadline = input("Enter deadline: ")
        category = input("Enter category: ")
        manager.add_task(title, deadline, category)

    elif choice == "2":
        manager.show_tasks()

    elif choice == "3":
        break

    else:
        print("Invalid choice")