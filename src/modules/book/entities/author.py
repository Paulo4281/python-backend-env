from src.database.base import Base
from sqlalchemy import String, DATETIME, DateTime, DATE, Date
from sqlalchemy.orm import Mapped, mapped_column
from typing import Dict

class Author(Base):

    __tablename__ = "tb_author"

    id_: Mapped[str] = mapped_column(primary_key=True, type_=String, name="id_author")
    name: Mapped[str] = mapped_column(type_=String, name="name_author")
    birth: Mapped[Date] = mapped_column(type_=DATE, name="birth_author")
    death: Mapped[Date] = mapped_column(type_=DATE, name="death_author")
    nationality: Mapped[Date] = mapped_column(type_=String, name="nationality_author")
    updated_at: Mapped[DateTime] = mapped_column(type_=DATETIME, name="updated_at")
    created_at: Mapped[DateTime] = mapped_column(type_=DATETIME, name="created_at")

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