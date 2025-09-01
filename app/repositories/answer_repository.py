from sqlalchemy import delete
from app.config.database import async_session
from app.repositories.model.answer import AnswersOrm
from app.routers.model import AnswerAdd, Answer
import logging

logger = logging.getLogger(__name__)


class AnswerRepository:

    @staticmethod
    async def add_answer(answer_data: AnswerAdd, question_id: int) -> AnswersOrm:
        logger.info(f"Received request to add answer to question {question_id}")
        async with async_session() as session:
            answer = AnswersOrm(**answer_data.dict(), question_id=question_id)
            session.add(answer)
            await session.commit()
            await session.refresh(answer)
            logger.info(f"Successfully added answer with ID: {answer.id}")
            return answer

    @staticmethod
    async def find_by_id(answer_id: int) -> Answer | None:
        logger.info(f"Received request to get answer with ID: {answer_id}")
        async with async_session() as session:
            db_answer = await session.get(AnswersOrm, answer_id)
            if db_answer:
                logger.info(f"Successfully retrieved answer with ID: {answer_id}")
                return Answer.model_validate(db_answer)
            else:
                logger.warning(f"Answer with ID {answer_id} not found")
                return None

    @staticmethod
    async def delete_by_id(answer_id: int) -> bool:
        logger.info(f"Received request to delete answer with ID: {answer_id}")
        async with async_session() as session:
            answer = await session.get(AnswersOrm, answer_id)
            if not answer:
                logger.warning(f"Answer with ID {answer_id} not found for deletion")
                return False
            await session.delete(answer)
            await session.commit()
            logger.info(f"Successfully deleted answer with ID: {answer_id}")
            return True

    @staticmethod
    async def delete_by_question_id(question_id: int) -> int:
        logger.info(f"Received request to delete answers for question ID: {question_id}")
        async with async_session() as session:
            stmt = delete(AnswersOrm).where(AnswersOrm.question_id == question_id)
            result = await session.execute(stmt)
            await session.commit()
            logger.info(f"Deleted {result.rowcount} answers for question ID: {question_id}")
            return result.rowcount
