from src.modules.user.dtos.user_dto import UserAuthDTO, UserDTO
from src.modules.user.entities.user import User
from src.modules.user.repositories.user_repository import UserRepository

class UserService:
    def auth(data: UserAuthDTO) -> any:
        return {
            "name": data["name"],
            "password": data["password"]
        }
    
    def save(data: UserDTO) -> User:
        return UserRepository.save(self=UserRepository, data=data)