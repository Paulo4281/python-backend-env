from flask_restx import  fields, Namespace
from src.modules.book.dtos.author_dto import AuthorDTO, AuthorResponseDTO
from typing import Any

class AuthorModel:
    def __init__(self, namespace: Namespace) -> None:
        self.namespace = namespace

    def save(self) -> Any:
        data_model: AuthorDTO = {
            "name": fields.String(),
            "birth": fields.String(),
            "death": fields.String(),
            "nationality": fields.String()
        }
        return self.namespace.model("author_save", data_model)
    
    def find(self) -> Any:
        return self.namespace.model("author_find", self.find_by_id())

    def find_by_id(self) -> Any:
        data_model: AuthorResponseDTO = {
            "id_": fields.String(),
            "name": fields.String(),
            "birth": fields.String(),
            "death": fields.String(),
            "nationality": fields.String(),
            "updated_at": fields.DateTime(),
            "created_at": fields.DateTime()
        }
        return self.namespace.model("author_find_by_id", data_model)
    
    def update(self) -> Any:
        return self.namespace.model("author_update", self.save())