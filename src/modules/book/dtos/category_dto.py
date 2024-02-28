from typing import TypedDict
from datetime import datetime

class CategoryDTO(TypedDict):
    name: str

class CategoryResponseDTO(TypedDict):
    id_: str
    name: str
    updated_at: datetime
    created_at: datetime

class CategoryUpdateDTO(CategoryDTO):
    pass