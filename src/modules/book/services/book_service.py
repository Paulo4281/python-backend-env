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
    
    @staticmethod
    def find_by_id(id_: str) -> BookResponseDTO:
        return BookRepository.find_by_id(id_)
    
    @staticmethod
    def update(id_: str, data: BookUpdateDTO) -> None:
        return BookRepository.update(id_, data)
    
    @staticmethod
    def delete(id_: str) -> None:
        return BookRepository.delete(id_)