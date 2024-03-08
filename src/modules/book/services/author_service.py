from src.modules.book.dtos.author_dto import AuthorDTO, AuthorResponseDTO
from src.modules.book.repositories.author_repository import AuthorRepository
from typing import List

class AuthorService:
    @staticmethod
    def save(data: AuthorDTO) -> AuthorResponseDTO:
        return AuthorRepository().save(data)
    
    @staticmethod
    def find() -> List[AuthorResponseDTO]:
        return AuthorRepository().find()
    
    @staticmethod
    def find_by_id(id_: str) -> AuthorResponseDTO:
        user = AuthorRepository().find_by_id(id_)
        if user:
            return user
        raise Exception("Not found.")

    @staticmethod
    def delete(id_: str) -> None:
        AuthorService().find_by_id(id_)
        AuthorRepository().delete(id_)