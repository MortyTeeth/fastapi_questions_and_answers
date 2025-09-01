from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime


class AnswerAdd(BaseModel):
    text: str
    user_id: int


class Answer(BaseModel):
    id: int
    text: str
    created_at: datetime
    question_id: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)


class QuestionWithAnswers(BaseModel):
    id: int
    text: str
    created_at: datetime
    answers: List[Answer]

    class Config:
        orm_mode = True
