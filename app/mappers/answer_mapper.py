from app.repositories.answer_repository import AnswersOrm
from app.services.model.answer import AnswerDomain
from app.routers.answer_router import Answer


class AnswerMapper:
    @staticmethod
    def do_to_domain(answer: AnswersOrm) -> AnswerDomain:
        return AnswerDomain(answer.id, answer.question_id, answer.user_id, answer.text, answer.created_at)

    @staticmethod
    def domain_to_dto(answer: AnswerDomain) -> Answer:
        return Answer(**vars(answer))
