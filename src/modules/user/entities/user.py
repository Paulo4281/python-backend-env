from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import Dict

Base = declarative_base()

class User(Base):
    __tablename__ = "tb_usuario"

    id_: Mapped[str] = mapped_column(primary_key=True, name="id_usuario")
    name: Mapped[str] = mapped_column(type_=String, name="nome_usuario")
    mail: Mapped[str] = mapped_column(type_=String, name="email_usuario")
    password: Mapped[str] = mapped_column(type_=String, name="senha_usuario")
    age: Mapped[int] = mapped_column(type_=Integer, name="idade_usuario")
    created_at: Mapped[DateTime] = mapped_column(type_=DateTime, name="criado_em")

    def to_dict(self) -> Dict:
        return {
            "id_": self.id_,
            "name": self.name,
            "mail": self.mail,
            "password": self.password,
            "age": self.age,
            "created_at": self.created_at
        }