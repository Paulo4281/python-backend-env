from src.modules.book.dtos.review_dto import ReviewDTO, ReviewResponseDTO, ReviewUpdateDTO
from src.modules.book.entities.review import Review
from src.database.database_config import session
from uuid import uuid4
from datetime import datetime
from typing import List

class ReviewRepository:
    @staticmethod
    def save(data: ReviewDTO) -> ReviewResponseDTO:
        try:
            with session.begin():
                review = Review(
                    id_ = uuid4(),
                    rate = data["rate"],
                    review = data["review"],
                    id_book = data["id_book"],
                    id_user = data["id_user"]
                ) 

                session.add(review)
            return review.to_dict()
        except:
            session.rollback()
        finally:
            session.close()