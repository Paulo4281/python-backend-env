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