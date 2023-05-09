from datetime import date


class Task:

    def __init__(self, id, title, description, status, priority, start:date, end:date) -> None:
        self.id = id #int
        self.title = title #str
        self.description = description #str
        self.status = status #tuple "ToDo", "Blocked", "In Progress", "Done", "Recurring", "Hidden" -- may move recurring off this section?
        self.priority = priority #int
        self.start = start #date
        self.end = end #date