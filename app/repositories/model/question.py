from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from app.config.database import Model


class QuestionsOrm(Model):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(nullable=False, server_default=func.now())

    answers = relationship(
        "AnswersOrm",
        back_populates="question",
        cascade="all, delete",
        passive_deletes=True
    )