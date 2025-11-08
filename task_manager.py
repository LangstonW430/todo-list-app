
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