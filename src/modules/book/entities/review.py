from src.database.base import Base
from sqlalchemy import String, INTEGER, DATETIME, DateTime, ForeignKey, TEXT
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Dict
from src.modules.book.entities.book import Book
from src.modules.user.entities.user import User

class Review(Base):

    __tablename__ = "tb_review"

    id_: Mapped[str] = mapped_column(primary_key=True, type_=String, name="id_review")
    rate: Mapped[int] = mapped_column(type_=INTEGER, name="rating_review")
    review: Mapped[str] = mapped_column(type_=TEXT, name="text_review")
    id_book: Mapped[str] = mapped_column(ForeignKey("tb_book.id_book"), type_=String, name="id_book")
    id_user: Mapped[str] = mapped_column(ForeignKey("tb_user.id_user"), type_=String, name="id_user")
    created_at: Mapped[DateTime] = mapped_column(type_=DATETIME, name="created_at")

    book: Mapped[Book] = relationship("Book", foreign_keys=[id_book])
    user: Mapped[User] = relationship("User", foreign_keys=[id_user])

    def to_dict(self) -> Dict:
        return {
            "id_": self.id,
            "rate": self.rate,
            "review": self.review,
            "book_id": self.book_id,
            "user_id": self.user_id,
            "created_at": self.created_at
        }