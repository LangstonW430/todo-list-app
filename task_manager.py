from task import Task
import json

class TaskManager:
    def __init__(self):
        self.tasks = []

    def __iter__(self):
        return iter(self.tasks)

    def add_task(self, task):
        self.tasks.append(task)
    
    def remove_task(self, task):
        self.tasks.remove(task)

    def task_at(self, index=0):
        return self.tasks[index] if 0 <= index < len(self.tasks) else None

    def list_task(self):
        for task, index in enumerate(self.tasks):
            print(f"{index}. {task.title} - Due: {task.due_date}")

    def sort_list(self, reverse=False):
        self.tasks.sort(key=lambda task: task.title.lower(), reverse=reverse)

    def is_sorted(self, reverse=False):
        for i in range(len(self.tasks) - 1): # iterate through the list
            if (reverse and self.tasks[i].title.lower() < self.tasks[i + 1].title.lower()) or (not reverse and self.tasks[i].title.lower() > self.tasks[i + 1].title.lower()):
                return False
        return True
    
    def save_to_file(self, filename="tasks.json"):
        with open(filename, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def load_from_file(self, filename="tasks.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.tasks = [Task.from_dict(item) for item in data]
        except FileNotFoundError:
            self.tasks = []
        except json.JSONDecodeError:
            print("Warning: tasks.json is corrupted or empty. Starting with an empty list.")
            self.tasks = []