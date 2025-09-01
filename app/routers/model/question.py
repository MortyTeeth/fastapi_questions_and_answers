from datetime import datetime
from pydantic import BaseModel, ConfigDict
from typing import List
from .answer import Answer


class QuestionAddRequest(BaseModel):
    text: str


class Question(BaseModel):
    id: int
    text: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class QuestionWithAnswers(Question):
    answers: List[Answer]


class QuestionId(BaseModel):
    ok: bool = True
    question_id: int
