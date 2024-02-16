from src.modules.book.dtos.book_dto import BookDTO, BookResponseDTO
from src.modules.book.repositories.book_repository import BookRepository

class BookService:
    @staticmethod
    def save(data: BookDTO) -> BookResponseDTO:
        return BookRepository.save(data)