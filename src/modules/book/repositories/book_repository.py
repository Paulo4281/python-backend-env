from src.modules.book.entities.book import Book
from src.database.database_config import session
from src.modules.book.dtos.book_dto import BookDTO, BookResponseDTO, BookUpdateDTO
from uuid import uuid4
from datetime import datetime
from typing import List

class BookRepository:
    @staticmethod
    def save(data: BookDTO) -> BookResponseDTO:
        try:
            with session.begin():
                book = Book(
                    id_ = uuid4(),
                    title = data["title"],
                    price = data["price"],
                    rate = data["rate"],
                    category_id = data["category_id"],
                    owner_id = data["owner_id"],
                    created_at = datetime.now()
                )

                session.add(book)

            return book.to_dict()
        except Exception as e:
            session.rollback()
            raise Exception(e)
        finally:
            session.close()

    @staticmethod
    def find() -> List[BookResponseDTO]:
        try:
            with session.begin():
                books = session.query(Book)

                books_list = []

                for book in books:
                    books_list.append(book.to_dict())
                return books_list
        except:
            session.rollback()
        finally:
            session.close()