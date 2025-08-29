from typing import Annotated

from fastapi import APIRouter, Depends

from repository import QuestionRepository
from schemas import QuestionAdd, Question, QuestionId

router = APIRouter(
    prefix="/questions",
    tags=["Questions"]
)


@router.post("/")
async def add_question(
        question: Annotated[QuestionAdd, Depends()]
) -> QuestionId:
    task_id = await QuestionRepository.add_one(question)
    return {"ok": True, "task_id": task_id}


@router.get("/")
async def get_questions() -> list[Question]:
    questions = await QuestionRepository.find_all()
    return questions
