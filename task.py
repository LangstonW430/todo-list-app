class Task:
    def __init__(self, title="Untitled Task", due_date=None, status="not started"):
        self.title = title
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "title": self.title,
            "due_date": self.due_date,
            "status": self.status
        }
    
    @staticmethod
    def from_dict(data):
        return Task(data["title"], data["due_date"], data["status"])