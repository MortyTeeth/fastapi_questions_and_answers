from fastapi import APIRouter, HTTPException, Depends
from app.routers.model import AnswerAdd, Answer
from app.services.answer_service import AnswerService
from app.repositories.answer_repository import AnswerRepository
from app.repositories.question_repository import QuestionRepository
from pydantic import BaseModel
from app.config.logging_config import logger

router = APIRouter(
    prefix="/answers",
    tags=["Answers"]
)


class MessageResponse(BaseModel):
    message: str


def get_answer_service() -> AnswerService:
    return AnswerService(
        answer_repository=AnswerRepository(),
        question_repository=QuestionRepository()
    )


@router.post("/questions/{question_id}/", response_model=Answer)
async def add_answer_to_question(

        question_id: int,
        answer_data: AnswerAdd,
        service: AnswerService = Depends(get_answer_service)
):
    logger.info(f"Received request to add an answer to question with ID: {question_id}")
    return await service.add_answer(question_id, answer_data)


@router.get("/{answer_id}", response_model=Answer)
async def get_answer_by_id(
        answer_id: int,
        service: AnswerService = Depends(get_answer_service)
):
    logger.info(f"Received request to get answer with ID: {answer_id}")
    try:
        answer = await service.get_answer_by_id(answer_id)
        logger.info(f"Successfully retrieved answer with ID: {answer.id}")
        return answer
    except ValueError as e:
        logger.error(f"Failed to retrieve answer with ID {answer_id}: {str(e)}")
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{answer_id}", response_model=MessageResponse)
async def delete_answer(
        answer_id: int,
        service: AnswerService = Depends(get_answer_service)
):
    logger.info(f"Received request to delete answer with ID: {answer_id}")
    try:
        await service.delete_answer_by_id(answer_id)
        logger.info(f"Answer with ID {answer_id} successfully deleted.")
        return {"message": "Answer deleted"}
    except ValueError as e:
        logger.error(f"Failed to delete answer with ID {answer_id}: {str(e)}")
        raise HTTPException(status_code=404, detail=str(e))
