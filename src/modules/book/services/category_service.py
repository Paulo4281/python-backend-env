from src.modules.book.dtos.category_dto import CategoryDTO, CategoryResponseDTO, CategoryUpdateDTO
from src.modules.book.repositories.category_repository import CategoryRepository
from typing import List

class CategoryService:
    @staticmethod
    def save(data: CategoryDTO) -> CategoryResponseDTO:
        return CategoryRepository.save(data)

    @staticmethod
    def find() -> List[CategoryResponseDTO]:
        return CategoryRepository.find()
    
    @staticmethod
    def find_by_id(id_: str) -> CategoryResponseDTO:
        category = CategoryRepository.find_by_id(id_)
        if category:
            return category
        raise Exception("Not found.")
    
    @staticmethod
    def update(id_: str, data: CategoryUpdateDTO) -> None:
        CategoryService().find_by_id(id_)
        CategoryRepository.update(id_, data)

    @staticmethod
    def delete(id_: str) -> None:
        CategoryService().find_by_id(id_)
        CategoryRepository.delete(id_)