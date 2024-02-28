from typing import TypedDict
from datetime import datetime

class BookDTO(TypedDict):
    title: str
    price: float
    rate: int
    category_id: str
    owner_id: str

class BookResponseDTO(TypedDict):
    id_: str
    title: str
    price: float
    rate: int
    category_id: str
    owner_id: str
    updated_at: datetime
    created_at: datetime

class BookUpdateDTO(BookDTO):
    pass