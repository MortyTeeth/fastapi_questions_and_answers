from app.repositories.question_repository import QuestionsOrm
from app.services.model.question import QuestionDomain
from app.routers.question_router import Question


class QuestionMapper:
    @staticmethod
    def do_to_domain(question: QuestionsOrm) -> QuestionDomain:
        return QuestionDomain(question.id, question.text, question.created_at)

    @staticmethod
    def domain_to_dto(question: QuestionDomain) -> Question:
        return Question(**vars(question))
