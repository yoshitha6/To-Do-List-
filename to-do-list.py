tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # View Tasks
    if choice == '1':
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(i, "-", task)

    # Add Task
    elif choice == '2':
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully!")

    # Delete Task
    elif choice == '3':
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(i, "-", task)

            try:
                task_num = int(input("Enter task number to delete: "))
                removed = tasks.pop(task_num - 1)
                print("Removed:", removed)
            except:
                print("Invalid task number")

    # Exit
    elif choice == '4':
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice")