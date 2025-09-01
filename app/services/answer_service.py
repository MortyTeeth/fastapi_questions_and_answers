from app.repositories.answer_repository import AnswerRepository
from app.repositories.question_repository import QuestionRepository
from app.routers.model import Answer, AnswerAdd
from app.mappers.answer_mapper import AnswerMapper, AnswerDomain


class AnswerService:
    def __init__(self, answer_repository: AnswerRepository, question_repository: QuestionRepository):
        self.answer_repository = answer_repository
        self.question_repository = question_repository

    async def add_answer(self, question_id: int, answer_data: AnswerAdd) -> AnswerDomain:
        if answer_data.text == "":
            raise HTTPException(status_code=400, detail="Answer should not be empty")
        question = await self.question_repository.find_by_id(question_id)
        if not question:
            raise HTTPException(status_code=404, detail="Question with id={} not found".format(question_id))

        return AnswerMapper.do_to_domain(await self.answer_repository.add_answer(answer_data, question_id))

    async def get_answer_by_id(self, answer_id: int) -> Answer:
        answer = await self.answer_repository.find_by_id(answer_id)
        if not answer:
            raise ValueError(f"Answer with id={answer_id} not found")
        return answer

    async def delete_answer_by_id(self, answer_id: int) -> bool:
        deleted = await self.answer_repository.delete_by_id(answer_id)
        if not deleted:
            raise ValueError(f"Answer with id={answer_id} not found")
        return deleted
