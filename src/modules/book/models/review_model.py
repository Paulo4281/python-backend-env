from flask_restx import fields, Namespace
from src.modules.book.dtos.review_dto import ReviewDTO, ReviewResponseDTO
from typing import Any

class ReviewModel:
    def __init__(self, namespace: Namespace) -> None:
        self.namespace= namespace

    def save(self) -> Any:
        data_model: ReviewDTO = {
            "rate": fields.Integer(),
            "review": fields.String(),
            "book_id": fields.String(),
            "user_id": fields.String()
        }
        return self.namespace.model("review_save", data_model)
    
    def find(self) -> Any:
        return self.namespace.model("review_find", self.find_by_id())

    def find_by_id(self) -> Any:
        data_model: ReviewResponseDTO = {
            "id_": fields.String(),
            "rate": fields.Integer(),
            "review": fields.String(),
            "book_id": fields.String(),
            "user_id": fields.String(),
            "updated_at": fields.DateTime(),
            "created_at": fields.DateTime()
        }
        return self.namespace.model("review_find_by_id", data_model)