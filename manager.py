from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, deadline, category):
        task = Task(title, deadline, category)
        self.tasks.append(task)

    def show_tasks(self):
        if not self.tasks:
            print("No tasks yet")
        else:
            for i, task in enumerate(self.tasks):
                status = "Done" if task.completed else "Not Done"
                print(f"{i+1}. {task.title} | {task.deadline} | {task.category} | {status}")