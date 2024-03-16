from src.modules.book.dtos.review_dto import ReviewDTO, ReviewUpdateDTO, ReviewResponseDTO
from src.modules.book.repositories.review_repository import ReviewRepository
from typing import List

class ReviewService:
    @staticmethod
    def save(data: ReviewDTO) -> ReviewResponseDTO:
        return ReviewRepository().save(data)
    
    @staticmethod
    def find() -> List[ReviewResponseDTO]:
        return ReviewRepository().find()
    
    @staticmethod
    def find_by_id(id_: str) -> ReviewResponseDTO:
        return ReviewRepository().find_by_id(id_)
    
    @staticmethod
    def update(id_: str, data: ReviewUpdateDTO) -> None:
        return ReviewRepository().update(id_, data)
    
    @staticmethod
    def delete(id_: str) -> None:
        return ReviewRepository().delete(id_)