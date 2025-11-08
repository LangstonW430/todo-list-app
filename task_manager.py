
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
        counter = 0
        for task in self.tasks:
            if counter == index:
                return self.tasks
            else:
                counter += 1

    def list_task(self):
        index = 1
        for task in  self.tasks:
            print(f"{index}. {task.title} - Due: {task.due_date}")
            index += 1

    def sort_list(self, reverse): #sorts by alpha order, reverse order if true
        while True:
            changed = False
            for i in range(len(self.tasks) - 1):
                if (reverse and self.tasks[i].title.lower() < self.tasks[i + 1].title.lower()) or (not reverse and self.tasks[i].title.lower() > self.tasks[i + 1].title.lower()):
                    self.tasks[i], self.tasks[i + 1] = self.tasks[i + 1], self.tasks[i]
                    changed = True
            if not changed:
                break

    def is_sorted(self, reverse=False):
        for i in range(len(self.tasks) - 1): # iterate through the list
            if (reverse and self.tasks[i].title.lower() < self.tasks[i + 1].title.lower()) or (not reverse and self.tasks[i].title.lower() > self.tasks[i + 1].title.lower()):
                return False
        return True