from datetime import datetime

from pydantic import BaseModel, ConfigDict


class QuestionAdd(BaseModel):
    text: str
    created_at: datetime


class Question(QuestionAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)


class QuestionId(BaseModel):
    ok: bool = True
    question_id: int
