from datetime import datetime


class QuestionDomain:
    def __init__(self, id: int, text: str, created_at: datetime):
        self.id = id
        self.text = text
        self.created_at = created_at
