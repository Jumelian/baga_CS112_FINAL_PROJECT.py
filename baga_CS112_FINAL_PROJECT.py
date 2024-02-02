class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the task list.")
    def view_tasks(self):
        if self.tasks:
            print("Tasks in the task list:")
            for task in self.tasks:
                print("-", task)
        else:
            print("Your task list is empty.")

def main():
    print("Welcome to the Task Management System!")
    task_manager = TaskManager()

    while True:
        print("\nMenu:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            task = input("Enter the task to add: ")
            task_manager.add_task(task)
        elif choice == '2':
            task_manager.view_tasks()
        elif choice == '3':
            print("Thank you for using the Task Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()