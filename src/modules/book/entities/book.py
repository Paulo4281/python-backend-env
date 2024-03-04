from src.database.base import Base
from sqlalchemy import DECIMAL, String, INTEGER, DATETIME, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Dict
from src.modules.book.entities.category import Category
from src.modules.user.entities.user import User

class Book(Base):

    __tablename__ = "tb_book"

    id_: Mapped[str] = mapped_column(primary_key=True, type_=String, name="id_book")
    title: Mapped[str] = mapped_column(type_=String, name="title_book")
    price: Mapped[float] = mapped_column(type_=DECIMAL, name="price_book")
    rate: Mapped[int] = mapped_column(type_=INTEGER, name="rate_book")
    category_id: Mapped[str] = mapped_column(ForeignKey("tb_category.id_category"), type_=String, name="id_category")
    owner_id: Mapped[str] = mapped_column(ForeignKey("tb_user.id_user"), type_=String, name="id_user")
    updated_at: Mapped[DateTime] = mapped_column(type_=DATETIME, name="updated_at")
    created_at: Mapped[DateTime] = mapped_column(type_=DATETIME, name="created_at")

    category: Mapped[Category] = relationship("Category", foreign_keys=[category_id])
    owner: Mapped[User] = relationship("User", foreign_keys=[owner_id])

    def to_dict(self) -> Dict:
        return {
            "id_": self.id_,
            "title": self.title,
            "price": float(self.price),
            "rate": self.rate,
            "category_id": self.category_id,
            "owner_id": self.owner_id,
            "updated_at": self.updated_at,
            "created_at": self.created_at,
        }