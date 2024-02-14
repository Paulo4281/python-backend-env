from src.modules.user.dtos.user_dto import UserAuthDTO, UserDTO, UserAuthResponseDTO
from src.modules.user.entities.user import User
from src.modules.user.repositories.user_repository import UserRepository
from typing import List

class UserService:
    @staticmethod
    def auth(data: UserAuthDTO) -> UserAuthResponseDTO:
        user = UserService.find_by_mail(data["mail"])

        return {
            "name": user["name"],
            "mail": user["mail"],
            "age": user["age"],
            "message": "Logado com sucesso! Sua sessão expira em 1h."
        }
    
    @staticmethod
    def save(data: UserDTO) -> User:
        return UserRepository.save(data)
    
    @staticmethod
    def find() -> List[User]:
        return UserRepository.find()
    
    @staticmethod
    def find_by_id(id: str) -> User:
        user = UserRepository.find_by_id(id)
        if user:
            return user
        raise Exception("Usuário não cadastrado.")
    
    @staticmethod
    def find_by_mail(mail: str) -> User:
        user = UserRepository.find_by_mail(mail)
        if user:
            return user
        raise Exception("E-mail não cadastrado.")
    
    @staticmethod
    def update(id_: str, data: UserDTO) -> None:
        if UserService.find_by_id(id_):
            UserRepository.update(id_, data)

    @staticmethod
    def delete(id_: str) -> None:
        if UserService.find_by_id(id_):
            UserRepository.delete(id_)