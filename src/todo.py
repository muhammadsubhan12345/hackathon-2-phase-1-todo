class Todo:
    def __init__(self, todo_id, title, description):
        self.id = todo_id
        self.title = title
        self.description = description
        self.completed = False
    
    def update(self, title=None, description=None):
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
    
    def toggle_complete(self):
        self.completed = not self.completed
    
    def __str__(self):
        status = "Completed" if self.completed else "Incomplete"
        return f"ID: {self.id}\nTitle: {self.title}\nDescription: {self.description}\nStatus: {status}"