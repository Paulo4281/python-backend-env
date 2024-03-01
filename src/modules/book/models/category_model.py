from flask_restx import fields, Namespace
from src.modules.book.dtos.category_dto import CategoryDTO, CategoryResponseDTO
from typing import Any

class CategoryModel:
    def __init__(self, namespace: Namespace) -> None:
        self.namespace = namespace

    def save(self) -> Any:
        data_model: CategoryDTO = {
            "name": fields.String()
        }
        return self.namespace.model("category_save", data_model)

    def find(self) -> Any:
        return self.namespace.model("category_find", self.find_by_id())

    def find_by_id(self) -> Any:
        data_model: CategoryResponseDTO = {
            "id_": fields.String(),
            "name": fields.String(),
            "updated_at": fields.DateTime(),
            "created_at": fields.DateTime()
        }
        return self.namespace.model("category_find_by_id", data_model)
    
    def update(self) -> Any:
        return self.namespace.model("category_update", self.save())