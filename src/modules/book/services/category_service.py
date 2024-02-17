from src.modules.book.dtos.category_dto import CategoryDTO, CategoryResponseDTO, CategoryUpdateDTO
from src.modules.book.repositories.category_repository import CategoryRepository
from typing import List

class CategoryService:
    @staticmethod
    def save(data: CategoryDTO) -> CategoryResponseDTO:
        return CategoryRepository.save(data)