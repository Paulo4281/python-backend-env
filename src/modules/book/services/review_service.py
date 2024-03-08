from src.modules.book.dtos.review_dto import ReviewDTO, ReviewResponseDTO
from src.modules.book.repositories.review_repository import ReviewRepository
from typing import List

class ReviewService:
    @staticmethod
    def save(data: ReviewDTO) -> ReviewResponseDTO:
        return ReviewRepository().save(data)