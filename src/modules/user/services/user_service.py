from src.modules.user.dtos.user_dto import UserAuthDTO, UserDTO, UserAuthResponseDTO, UserResponseDTO, UserUpdateDTO
from src.modules.user.repositories.user_repository import UserRepository
from typing import List
from bcrypt import checkpw
from jwt import encode
from dotenv import load_dotenv
from os import getenv
from datetime import datetime, timezone, timedelta

load_dotenv()

class UserService:
    @staticmethod
    def auth(data: UserAuthDTO) -> UserAuthResponseDTO:
        user = UserService.__find_by_mail(data["mail"])
        user_password = UserRepository.get_user_password(user["id_"])
        if checkpw(bytes(data["password"], "utf8"), bytes(user_password, "utf8")):
            return {
                "token": encode(payload={"sub": getenv("TOKEN_SUB"), "iat": datetime.now(tz=timezone.utc), "exp": datetime.now(tz=timezone.utc) + timedelta(days=1)}, key=getenv("TOKEN_SECRET"))
            }
        else:
            raise Exception("E-mail ou senha incorretos.")
    
    @staticmethod
    def save(data: UserDTO) -> UserResponseDTO:
        return UserRepository.save(data)
    
    @staticmethod
    def find() -> List[UserResponseDTO]:
        return UserRepository.find()
    
    @staticmethod
    def find_by_id(id: str) -> UserResponseDTO:
        user = UserRepository.find_by_id(id)
        if user:
            return user
        raise Exception("Usuário não cadastrado.")
    
    
    @staticmethod
    def update(id_: str, data: UserUpdateDTO) -> None:
        if UserService.find_by_id(id_):
            UserRepository.update(id_, data)

    @staticmethod
    def delete(id_: str) -> None:
        if UserService.find_by_id(id_):
            UserRepository.delete(id_)

    @staticmethod
    def __find_by_mail(mail: str) -> UserResponseDTO:
        user = UserRepository.find_by_mail(mail)
        if user:
            return user
        raise Exception("E-mail não cadastrado.")