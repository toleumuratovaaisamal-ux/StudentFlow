class Task:
    def __init__(self, title, deadline, category):
        self.title = title
        self.deadline = deadline
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            "title": self.title,
            "deadline": self.deadline,
            "category": self.category,
            "completed": self.completed
        }