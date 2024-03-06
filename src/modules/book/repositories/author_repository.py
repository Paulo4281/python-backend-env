from src.modules.book.entities.author import Author
from src.database.database_config import session
from src.modules.book.dtos.author_dto import AuthorDTO, AuthorResponseDTO, AuthorUpdateDTO
from uuid import uuid4
from datetime import datetime
from typing import List

class AuthorRepository:

    @staticmethod
    def save(data: AuthorDTO) -> AuthorResponseDTO:
        try:
            with session.begin():
                author = Author(
                    id_ = uuid4(),
                    name = data["name"],
                    birth = data["birth"],
                    death = data["death"],
                    nationality = data["nationality"],
                    updated_at = None,
                    created_at = datetime.now()
                )

                session.add(author)

            return author.to_dict()
        except:
            session.rollback()
        finally:
            session.close()

    @staticmethod
    def find() -> List[AuthorResponseDTO]:
        try:
            with session.begin():
                authors = session.query(Author)

                authors_list = []

                for author in authors:
                    authors_list.append(author.to_dict())

            return authors_list
        except:
            session.rollback()
        finally:
            session.close()

    @staticmethod
    def find_by_id(id_: str) -> AuthorResponseDTO:
        try:
            with session.begin():
                author = session.query(Author).filter(Author.id_ == id_).first()

                return author.to_dict()
        except:
            session.rollback()
        finally:
            session.close()

    @staticmethod
    def update(id_: str, data: AuthorUpdateDTO) -> None:
        try:
            with session.begin():
                session.query(Author).filter(Author.id_ == id_).update(data)
        except:
            session.rollback()
        finally:
            session.close()

    @staticmethod
    def delete(id_: str) -> None:
        try:
            with session.begin():
                session.query(Author).filter(Author.id_ == id_).delete()
        except:
            session.rollback()
        finally:
            session.close()