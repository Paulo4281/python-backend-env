from src.modules.book.dtos.author_dto import AuthorDTO, AuthorResponseDTO, AuthorUpdateDTO
from src.modules.book.repositories.author_repository import AuthorRepository
from typing import List

class AuthorService:
    @staticmethod
    def save(data: AuthorDTO) -> AuthorResponseDTO:
        return AuthorRepository().save(data)