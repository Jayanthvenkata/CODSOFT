class Task:
    """Represents a single task in the To-Do list."""
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        """Mark the task as completed."""
        self.completed = True

    def __str__(self):
        """Return the string representation of the task."""
        status = "Completed" if self.completed else "Pending"
        return f"{self.description} - {status}"


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Task '{description}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to show.")
            return
        print("\nYour To-Do List:")
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task}")

    def delete_task(self, task_number):
        if task_number < 1 or task_number > len(self.tasks):
            print("Invalid task number.")
        else:
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task.description}' deleted.")

    def mark_task_completed(self, task_number):
        if task_number < 1 or task_number > len(self.tasks):
            print("Invalid task number.")
        else:
            self.tasks[task_number - 1].mark_completed()
            print(f"Task marked as completed.")

    def show_menu(self):
        while True:
            print("\nTo-Do List Menu:")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Delete a task")
            print("4. Mark task as completed")
            print("5. Exit")
            
            try:
                choice = int(input("Enter your choice: "))
                
                if choice == 1:
                    description = input("Enter task description: ")
                    self.add_task(description)
                elif choice == 2:
                    self.view_tasks()
                elif choice == 3:
                    task_number = int(input("Enter task number to delete: "))
                    self.delete_task(task_number)
                elif choice == 4:
                    task_number = int(input("Enter task number to mark as completed: "))
                    self.mark_task_completed(task_number)
                elif choice == 5:
                    print("Exiting To-Do List. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    todo_list = TodoList()
    todo_list.show_menu()
