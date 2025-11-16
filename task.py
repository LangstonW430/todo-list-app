from datetime import date

class Task:
    def __init__(self, title, due_date : date, status="not started"):
        self.title = title
        self.due_date = due_date
        self.status = status

    @property
    def remaining_time(self):
        if self.due_date:
            return self.due_date - date.today()
        return None

    def to_dict(self):
        return {
            "title": self.title,
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "status": self.status
        }
    
    def calculate_remaining_time(self):
        if self.due_date:
            return self.due_date - date.today()
        return None
    
    @staticmethod
    def from_dict(data):
        due_date = (
            date.fromisoformat(data["due_date"]) if data["due_date"] else None
        )
        return Task(data["title"], due_date, data["status"])