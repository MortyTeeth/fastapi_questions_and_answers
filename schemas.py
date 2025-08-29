from datetime import datetime

from pydantic import BaseModel, Field


class QuestionAdd(BaseModel):
    text: str
    created_at: datetime


class Question(QuestionAdd):
    id: int


class QuestionId(BaseModel):
    ok: bool = True
    question_id: int
