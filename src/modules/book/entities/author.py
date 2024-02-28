from src.database.base import Base
from sqlalchemy import String, DATETIME, DateTime, DATE, Date
from sqlalchemy.orm import Mapped, mapped_column
from typing import Dict

class Author(Base):

    __tablename__ = "tb_autor"

    id_: Mapped[str] = mapped_column(primary_key=True, type_=String, name="id_autor")
    name: Mapped[str] = mapped_column(type_=String, name="nome_autor")
    birth: Mapped[Date] = mapped_column(type_=DATE, name="dtnascimento_autor")
    death: Mapped[Date] = mapped_column(type_=DATE, name="dtfalecimento_autor")
    nationality: Mapped[Date] = mapped_column(type_=String, name="nacionalidade_autor")
    updated_at: Mapped[DateTime] = mapped_column(type_=DATETIME, name="atualizado_em")
    created_at: Mapped[DateTime] = mapped_column(type_=DATETIME, name="criado_em")

    def to_dict(self) -> Dict:
        return {
            "id_": self.id_,
            "name": self.name,
            "birth": self.birth,
            "death": self.death,
            "nationality": self.nationality,
            "updated_at": self.updated_at,
            "created_at": self.created_at
        }