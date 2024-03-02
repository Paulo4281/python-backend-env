from src.database.base import Base
from sqlalchemy import String, DATETIME, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from typing import Dict

class Category(Base):
    __tablename__ = "tb_category"

    id_: Mapped[str] = mapped_column(primary_key=True, type_=String, name="id_category")
    name: Mapped[str] = mapped_column(type_=String, name="name_category")
    updated_at: Mapped[DateTime] = mapped_column(type_=DATETIME, name="updated_at")
    created_at: Mapped[DateTime] = mapped_column(type_=DATETIME, name="created_at")

    def to_dict(self) -> Dict:
        return {
            "id_": self.id_,
            "name": self.name,
            "updated_at": self.updated_at,
            "created_at": self.created_at
        }