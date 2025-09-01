from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from app.config.database import Model


class AnswersOrm(Model):
    __tablename__ = "answers"

    id: Mapped[int] = mapped_column(primary_key=True)
    question_id: Mapped[int] = mapped_column(ForeignKey("questions.id", ondelete="CASCADE"), nullable=False)
    user_id: Mapped[int]
    text: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(default=func.now())

    question = relationship("QuestionsOrm", back_populates="answers")
