from src.modules.book.entities.book import Book
from src.database.database_config import session
from src.modules.book.dtos.book_dto import BookDTO, BookResponseDTO
from uuid import uuid4
from datetime import datetime

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
                    category = data["category"],
                    owner = data["owner"],
                    created_at = datetime.now()
                )

                session.add(book)

            return book.to_dict()
        except:
            session.rollback()
        finally:
            session.close()