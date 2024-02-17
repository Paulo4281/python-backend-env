from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from typing import Dict

Base = declarative_base()

class Category(Base):
    __tablename__ = "tb_categoria"

    id_: Mapped[str] = mapped_column(primary_key=True, type_=String, name="id_categoria")
    name: Mapped[str] = mapped_column(type_=String, name="nome_categoria")
    created_at: Mapped[DateTime] = mapped_column(type_=DateTime, name="criado_em")

    def to_dict(self) -> Dict:
        return {
            "id_": self.id_,
            "name": self.name,
            "created_at": self.created_at
        }