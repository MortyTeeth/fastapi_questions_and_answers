from database import new_session, QuestionsOrm
from schemas import QuestionAdd, Question
from sqlalchemy import select


class QuestionRepository:
    @classmethod
    async def add_one(cls, data: QuestionAdd) -> int:
        async with new_session() as session:
            question_dict = data.model_dump()

            question = QuestionsOrm(**question_dict)
            session.add(question)
            await session.flush()
            await session.commit()
            return question.id

    @classmethod
    async def find_all(cls) -> list[Question]:
        async with new_session() as session:
            query = select(QuestionsOrm)
            result = await session.execute(query)
            question_models = result.scalars().all()
            question_schemas = [Question.model_validate(question_model) for question_model in question_models]
            return question_schemas

    @staticmethod
    async def find_by_id(id: int) -> object:
        async with new_session() as session:
            result = await session.get(QuestionsOrm, id)
            return result

    @staticmethod
    async def delete_by_id(id: int):
        async with new_session() as session:
            question = await session.get(QuestionsOrm, id)
            if not question:
                return False
            await session.delete(question)
            await session.commit()
            return True
