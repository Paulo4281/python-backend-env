from typing import TypedDict

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
    created_at: str

class BookUpdateDTO(BookDTO):
    pass