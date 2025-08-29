from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

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
    question_id = await QuestionRepository.add_one(question)
    return {"ok": True, "question_id": question_id}


@router.get("/")
async def get_questions() -> list[Question]:
    questions = await QuestionRepository.find_all()
    return questions


@router.get("/{id}")
async def get_question_by_id(id: int):
    question = await QuestionRepository.find_by_id(id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return question


@router.delete("/{id}")
async def delete_question(id: int):
    deleted = await QuestionRepository.delete_by_id(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Question not found")
    return {"message": "Question deleted"}
