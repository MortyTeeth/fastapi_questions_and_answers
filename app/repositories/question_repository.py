from typing import List
from sqlalchemy import select
from app.repositories.model.question import QuestionsOrm
from app.config.database import async_session
from app.routers.model import QuestionAddRequest, Question
import logging

logger = logging.getLogger(__name__)


class QuestionRepository:

    @classmethod
    async def add_one(cls, data: QuestionAddRequest) -> QuestionsOrm:
        logger.info(f"Received request to add a question: {data.text}")
        async with async_session() as session:
            question_dict = data.model_dump()
            question = QuestionsOrm(**question_dict)
            session.add(question)
            await session.flush()
            await session.commit()
            logger.info(f"Successfully added question with ID: {question.id}")
            return question

    @classmethod
    async def find_all(cls) -> List[Question]:
        logger.info("Received request to get all questions")
        async with async_session() as session:
            result = await session.execute(select(QuestionsOrm))
            questions = result.scalars().all()
            logger.info(f"Returning {len(questions)} questions")
            return [Question.model_validate(q) for q in questions]

    @classmethod
    async def find_by_id(cls, id: int) -> QuestionsOrm | None:
        logger.info(f"Received request to get question with ID: {id}")
        async with async_session() as session:
            question = await session.get(QuestionsOrm, id)
            if question:
                logger.info(f"Found question with ID: {id}")
            else:
                logger.warning(f"Question with ID {id} not found")
            return question

    @classmethod
    async def delete_by_id(cls, id: int) -> bool:
        logger.info(f"Received request to delete question with ID: {id}")
        async with async_session() as session:
            question = await session.get(QuestionsOrm, id)
            if not question:
                logger.warning(f"Question with ID {id} not found for deletion")
                return False
            await session.delete(question)
            await session.commit()
            logger.info(f"Successfully deleted question with ID: {id}")
            return True
