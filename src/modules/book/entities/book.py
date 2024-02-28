from src.database.base import Base
from sqlalchemy import DECIMAL, String, INTEGER, DATETIME, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Dict
from src.modules.book.entities.category import Category
from src.modules.user.entities.user import User

class Book(Base):

    __tablename__ = "tb_livro"

    id_: Mapped[str] = mapped_column(primary_key=True, type_=String, name="id_livro")
    title: Mapped[str] = mapped_column(type_=String, name="titulo_livro")
    price: Mapped[float] = mapped_column(type_=DECIMAL, name="preco_livro")
    rate: Mapped[int] = mapped_column(type_=INTEGER, name="avaliacao_livro")
    category_id: Mapped[str] = mapped_column(ForeignKey("tb_categoria.id_categoria"), type_=String, name="id_categoria")
    owner_id: Mapped[str] = mapped_column(ForeignKey("tb_usuario.id_usuario"), type_=String, name="id_usuario")
    updated_at: Mapped[DateTime] = mapped_column(type_=DATETIME, name="atualizado_em")
    created_at: Mapped[DateTime] = mapped_column(type_=DATETIME, name="criado_em")

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