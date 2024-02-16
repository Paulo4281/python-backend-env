from typing import TypedDict

class BookDTO(TypedDict):
    title: str
    price: float
    rate: int
    category: str
    owner: str

class BookResponseDTO(TypedDict):
    id_: str
    title: str
    price: float
    rate: int
    category: str
    owner: str
    created_at: str