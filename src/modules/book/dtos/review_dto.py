from typing import TypedDict
from datetime import datetime

class ReviewDTO(TypedDict):
    rate: int
    review: str
    id_user: str
    id_book: str

class ReviewResponseDTO(ReviewDTO):
    id_: str
    created_at: datetime

class ReviewUpdateDTO(ReviewDTO):
    pass
