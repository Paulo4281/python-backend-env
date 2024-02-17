from src.modules.book.entities.category import Category
from src.database.database_config import session
from src.modules.book.dtos.category_dto import CategoryDTO, CategoryResponseDTO, CategoryUpdateDTO
from uuid import uuid4
from datetime import datetime
from typing import List

class CategoryRepository:
    @staticmethod
    def save(data: CategoryDTO) -> CategoryResponseDTO:
        try:
            with session.begin():
                category = Category(
                    id_ = uuid4(),
                    name = data["name"],
                    created_at = datetime.now()
                )

                session.add(category)

            return category.to_dict()
        except:
            session.rollback()
        finally:
            session.close()