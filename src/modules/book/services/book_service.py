from src.modules.book.dtos.book_dto import BookDTO, BookResponseDTO, BookUpdateDTO
from src.modules.book.repositories.book_repository import BookRepository
from typing import List

class BookService:
    @staticmethod
    def save(data: BookDTO) -> BookResponseDTO:
        return BookRepository.save(data)

    @staticmethod
    def find() -> List[BookResponseDTO]:
        return BookRepository.find()