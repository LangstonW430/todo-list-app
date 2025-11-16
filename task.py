from datetime import datetime

class Task:
    def __init__(self, title, due_date=None, status="not started"):
        self.title = title
        self.due_date = due_date
        self.status = status
        self.remaining_time = self.calculate_remaining_time()

    def to_dict(self):
        return {
            "title": self.title,
            "due_date": self.due_date,
            "status": self.status
        }
    
    def calculate_remaining_time(self):
        if self.due_date:
            return self.due_date - datetime.now()
        return None
    
    @staticmethod
    def from_dict(data):
        return Task(data["title"], data["due_date"], data["status"])