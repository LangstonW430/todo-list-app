from datetime import datetime

class Task:
    def __init__(self, title, due_date : datetime, status="not started"):
        self.title = title
        self.due_date = due_date
        self.status = status
        print(type(self.due_date))

    @property
    def remaining_time(self):
        if self.due_date:
            return self.due_date - datetime.now()
        return None

    def to_dict(self):
        return {
            "title": self.title,
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "status": self.status
        }
    
    def calculate_remaining_time(self):
        if self.due_date:
            return self.due_date - datetime.now()
        return None
    
    @staticmethod
    def from_dict(data):
        due_date = (
            datetime.fromisoformat(data["due_date"])
            if data["due_date"]
            else None
        )
        return Task(data["title"], due_date, data["status"])