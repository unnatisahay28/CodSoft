class ToDoList:
    def __init__(self):
        self.tasks = []

    def show_tasks(self):
        if not self.tasks:
            print("You have no tasks.")
        else:
            print("Your tasks:")
            for i, task in enumerate(self.tasks, 1):
                status = "[X]" if task["done"] else "[ ]"
                print(f"{i}. {task['task']} {status}")

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        print(f"Task '{task}' added.")

    def delete_task(self, task_number):
        try:
            del self.tasks[task_number - 1]
            print(f"Task {task_number} deleted.")
        except IndexError:
            print(f"Task {task_number} does not exist.")

    def mark_done(self, task_number):
        try:
            self.tasks[task_number - 1]["done"] = True
            print(f"Task {task_number} marked as done.")
        except IndexError:
            print(f"Task {task_number} does not exist.")

def main():
    todo = ToDoList()

    while True:
        print("\n1. Show tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Mark task as done")
        print("5. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            todo.show_tasks()
        elif choice == "2":
            task = input("Enter a task: ")
            todo.add_task(task)
        elif choice == "3":
            task_number = int(input("Enter the task number to delete: "))
            todo.delete_task(task_number)
        elif choice == "4":
            task_number = int(input("Enter the task number to mark as done: "))
            todo.mark_done(task_number)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()