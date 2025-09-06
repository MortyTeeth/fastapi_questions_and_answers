from app.repositories.question_repository import QuestionRepository
from app.routers.model import Question, QuestionAddRequest
from typing import List
from app.mappers.question_mapper import QuestionMapper
from app.services.model.question import QuestionDomain
from fastapi import HTTPException


class QuestionService:
    def __init__(self, repository: QuestionRepository):
        self.repository = repository

    async def list_questions(self) -> List[Question]:
        return await self.repository.find_all()

    async def get_question(self, qid: int) -> Question:
        question = await self.repository.find_by_id(qid)
        if not question:
            raise HTTPException(status_code=404, detail="Question with id={} not found".format(qid))
        return QuestionMapper.domain_to_dto(QuestionMapper.do_to_domain(question))

    async def add_question(self, data: QuestionAddRequest) -> QuestionDomain:
        if data.text == '':
            raise ValueError("Question should not be empty")
        return QuestionMapper.do_to_domain(await self.repository.add_one(data))

    async def delete_question(self, qid: int):
        success = await self.repository.delete_by_id(qid)
        if not success:
            raise HTTPException(status_code=404, detail="Question with id={} not found".format(qid))
