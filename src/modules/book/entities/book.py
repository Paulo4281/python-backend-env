from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import DECIMAL, String, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from typing import Dict

Base = declarative_base()

class Book(Base):
    __tablename__ = "tb_livro"

    id_: Mapped[str] = mapped_column(primary_key=True, type_=String, name="id_livro")
    title: Mapped[str] = mapped_column(type_=String, name="titulo_livro")
    price: Mapped[float] = mapped_column(type_=DECIMAL, name="preco_livro")
    rate: Mapped[int] = mapped_column(type_=Integer, name="avaliacao_livro")
    category: Mapped[str] = mapped_column(type_=String, name="id_categoria")
    owner: Mapped[str] = mapped_column(type_=String, name="id_usuario")
    created_at: Mapped[DateTime] = mapped_column(type_=DateTime, name="criado_em")

    def to_dict(self) -> Dict:
        return {
            "id_": self.id_,
            "title": self.title,
            "price": self.price,
            "rate": self.rate,
            "category": self.category,
            "owner": self.owner,
            "created_at": self.created_at
        }