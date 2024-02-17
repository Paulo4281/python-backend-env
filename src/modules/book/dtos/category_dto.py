from typing import TypedDict

class CategoryDTO(TypedDict):
    name: str

class CategoryResponseDTO(TypedDict):
    id_: str
    name: str
    created_at: str

class CategoryUpdateDTO(CategoryDTO):
    pass