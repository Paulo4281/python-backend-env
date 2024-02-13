from src.modules.user.entities.user import User
from src.modules.user.dtos.user_dto import UserDTO
from src.database.database_config import session
from src.utils.app_error import AppError
from typing import List
from uuid import uuid4
import datetime

class UserRepository:
    @staticmethod
    def save(data: UserDTO) -> User:
        try:
            with session.begin():
                user = User(
                        id = uuid4(),
                        name = data["name"],
                        mail = data["mail"],
                        password = data["password"],
                        age = data["age"],
                        created_at = datetime.datetime.now()
                )

                session.add(user)

            return user.to_dict()
        except Exception:
            session.rollback()

    @staticmethod
    def find() -> List[User]:
        try:
            with session.begin():
                users = session.query(User)

                users_list = []

                for user in users:
                    users_list.append(user.to_dict())
                    
            return users_list
        except Exception:
            session.rollback()
            
    @staticmethod
    def find_by_id(id: str) -> User:
        try:
            with session.begin():
                user = session.query(User).filter(User.id==id).first()

            return user.to_dict()
        except Exception:
            session.rollback()

    @staticmethod
    def find_by_mail(mail: str) -> User:
        try:
            if session.connection():
                session.close()
            with session.begin():
                user = session.query(User).filter(User.mail==mail).first()

            session.commit()
            return user.to_dict()
        except Exception:
            session.rollback()

    @staticmethod
    def update(id: str, data: UserDTO) -> None:
        try:
            if session.connection():
                session.close()

            with session.begin():
                session.query(User).filter(User.id==id).update(data)
                
        except Exception:
            session.rollback()

    @staticmethod
    def delete(id: str) -> None:
        try:
            if session.connection():
                session.close()

            with session.begin():
                session.query(User).filter(User.id==id).delete()

        except Exception:
            session.rollback()