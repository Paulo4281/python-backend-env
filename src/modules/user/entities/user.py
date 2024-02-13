from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from typing import Dict

Base = declarative_base()

class User(Base):
    __tablename__ = "tb_usuario"

    id = Column(String, name="id_usuario", primary_key=True)
    name = Column(String, name="nome_usuario")
    mail = Column(String, name="email_usuario")
    password = Column(String, name="senha_usuario")
    age = Column(Integer, name="idade_usuario")
    created_at = Column(DateTime, name="criado_em")

    def toDict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "mail": self.mail,
            "password": self.password,
            "age": self.age,
            "created_at": self.created_at
        }