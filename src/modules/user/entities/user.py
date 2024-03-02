from src.database.base import Base
from sqlalchemy import String, DATETIME, DateTime, DATE, Date
from sqlalchemy.orm import Mapped, mapped_column
from typing import Dict

class User(Base):
    __tablename__ = "tb_user"

    id_: Mapped[str] = mapped_column(primary_key=True, type_=String, name="id_user")
    name: Mapped[str] = mapped_column(type_=String, name="name_user")
    mail: Mapped[str] = mapped_column(type_=String, name="mail_user")
    password: Mapped[str] = mapped_column(type_=String, name="password_user")
    birth: Mapped[Date] = mapped_column(type_=DATE, name="birth_user")
    updated_at: Mapped[DateTime] = mapped_column(type_=DATETIME, name="updated_at")
    created_at: Mapped[DateTime] = mapped_column(type_=DATETIME, name="created_at")

    def to_dict(self) -> Dict:
        return {
            "id_": self.id_,
            "name": self.name,
            "mail": self.mail,
            "birth": self.birth,
            "updated_at": self.updated_at,
            "created_at": self.created_at
        }