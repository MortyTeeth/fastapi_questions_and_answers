from datetime import datetime


class AnswerDomain:
    def __init__(self, id: int, question_id: int, user_id: int, text: str, created_at: datetime):
        self.id = id
        self.question_id = question_id
        self.user_id = user_id
        self.text = text
        self.created_at = created_at
