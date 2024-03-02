from src.modules.book.dtos.author_dto import AuthorDTO, AuthorResponseDTO, AuthorUpdateDTO
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
        return AuthorRepository().find_by_id(id_)