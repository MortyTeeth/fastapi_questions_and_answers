from fastapi import APIRouter, Depends
from typing import List
from app.routers.model import QuestionAddRequest, Question
from app.repositories.question_repository import QuestionRepository
from app.services.question_service import QuestionService
from app.config.logging_config import logger

router = APIRouter(
    prefix="/questions",
    tags=["Questions"]
)


def get_question_service() -> QuestionService:
    return QuestionService(QuestionRepository())


@router.post("/", response_model=Question)
async def add_question(
        question: QuestionAddRequest,
        service: QuestionService = Depends(get_question_service)
):
    logger.info(f"Received request to create a new question: {question.text}")
    return await service.add_question(question)


@router.get("/", response_model=List[Question])
async def get_questions(
        service: QuestionService = Depends(get_question_service)
):
    logger.info("Received request to get all questions")
    questions = await service.list_questions()
    logger.info(f"Returning {len(questions)} questions")
    return questions


@router.get("/{id}", response_model=Question)
async def get_question_by_id(
        id: int,
        service: QuestionService = Depends(get_question_service)
):
    logger.info(f"Received request to get question with ID: {id}")
    return await service.get_question(id)


@router.delete("/{id}")
async def delete_question(
        id: int,
        service: QuestionService = Depends(get_question_service)
):
    logger.info(f"Received request to delete question with ID: {id}")
    await service.delete_question(id)
    return {"message": "Question deleted"}
