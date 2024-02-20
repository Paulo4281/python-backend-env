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

    @staticmethod
    def find() -> List[CategoryResponseDTO]:
        try:
            with session.begin():
                categories = session.query(Category)

                categories_list = []

                for category in categories:
                    categories_list.append(category.to_dict())

                return categories_list
        except:
            session.rollback()
        finally:
            session.close()

    @staticmethod
    def find_by_id(id_: str) -> CategoryResponseDTO:
        try:
            with session.begin():
                category = session.query(Category).filter(Category.id_ == id_).first()

                return category.to_dict()
        except:
            session.rollback()
        finally:
            session.close()

    @staticmethod
    def update(id_: str, data: CategoryDTO) -> None:
        try:
            with session.begin():
                session.query(Category).filter(Category.id_ == id_).update(data)
        except:
            session.rollback()
        finally:
            session.close()

    @staticmethod
    def delete(id_: str) -> None:
        try:
            with session.begin():
                session.query(Category).filter(Category.id_ == id_).delete()
        except:
            session.rollback()
        finally:
            session.close()