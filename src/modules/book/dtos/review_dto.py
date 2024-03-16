from typing import TypedDict
from datetime import datetime

class ReviewDTO(TypedDict):
    rate: int
    review: str
    user_id: str
    book_id: str

class ReviewResponseDTO(ReviewDTO):
    id_: str
    updated_at: datetime
    created_at: datetime

class ReviewUpdateDTO(ReviewDTO):
    pass
