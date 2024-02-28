from flask_restx import fields, Namespace
from typing import Any

class BookModel:
    def __init__(self, namespace: Namespace) -> None:
        self.namespace = namespace

    def save(self) -> Any:
        data_model = {
            "title": fields.String(),
            "price": fields.Float(),
            "rate": fields.Integer(),
            "category_id": fields.String(),
            "owner_id": fields.String()
        }
        return self.namespace.model("book_save", data_model)

    def find(self) -> Any:
        return self.namespace.model("book_find", self.find_by_id())

    def find_by_id(self) -> Any:
        data_model = {
            "id_": fields.String(),
            "title": fields.String(),
            "price": fields.Float(),
            "rate": fields.Integer(),
            "category_id": fields.String(),
            "owner_id": fields.String(),
            "updated_at": fields.DateTime(),
            "created_at": fields.DateTime()
        }
        return self.namespace.model("book_find_by_id", data_model)
    
    def update(self) -> Any:
        return self.namespace.model("book_update", self.save())