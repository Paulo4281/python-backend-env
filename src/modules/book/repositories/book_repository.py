from src.modules.book.entities.book import Book
from src.modules.book.entities.category import Category
from src.modules.book.entities.author import Author
from src.modules.user.entities.user import User
from src.database.database_config import session
from src.modules.book.dtos.book_dto import BookDTO, BookResponseDTO, BookUpdateDTO
from sqlalchemy.orm import joinedload
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
                    category_id = data["category_id"],
                    user_id = data["user_id"],
                    author_id = data["author_id"],
                    created_at = datetime.now()
                )

                session.add(book)

            return book.to_dict()
        except:
            session.rollback()
        finally:
            session.close()

    @staticmethod
    def find() -> List[BookResponseDTO]:
        try:
            with session.begin():
                books = session.query(Book, Category, Author, User).join(Category).join(Author).join(User).options(joinedload(Book.category), joinedload(Book.author), joinedload(Book.user))

                books_list = []

                for book, category, author, user in books:
                    book_dict = book.to_dict()
                    book_dict["category"] = category.to_dict()
                    book_dict["author"] = author.to_dict()
                    book_dict["user"] = user.to_dict()
                    books_list.append(book_dict)
            return books_list
        except:
            session.rollback()
        finally:
            session.close()

    @staticmethod
    def find_by_id(id_: str) -> BookResponseDTO:
        try:
            with session.begin():
                book = session.query(Book).filter(Book.id_ == id_).first()

            return book.to_dict()
        except:
            session.rollback()
        finally:
            session.close()

    @staticmethod
    def update(id_: str, data: BookUpdateDTO) -> None:
        try:
            with session.begin():
                session.query(Book).filter(Book.id_ == id_).update(data)
        except:
            session.rollback()
        finally:
            session.close()

    @staticmethod
    def delete(id_: str) -> None:
        try:
            with session.begin():
                session.query(Book).filter(Book.id_ == id_).delete()
        except:
            session.rollback()
        finally:
            session.close()