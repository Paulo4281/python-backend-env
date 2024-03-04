from src.modules.user.entities.user import User
from src.modules.user.dtos.user_dto import UserDTO, UserResponseDTO, UserUpdateDTO, UserPasswordResponseDTO
from src.database.database_config import session
from bcrypt import gensalt, hashpw
from typing import List
from uuid import uuid4
from datetime import datetime

class UserRepository:
    @staticmethod
    def save(data: UserDTO) -> UserResponseDTO:
        try:
            with session.begin():
                user = User(
                        id_ = uuid4(),
                        name = data["name"],
                        mail = data["mail"],
                        password = hashpw(data["password"].encode("utf8"), gensalt()),
                        birth = data["birth"],
                        updated_at = None,
                        created_at = datetime.now()
                )

                session.add(user)

            return user.to_dict()
        except Exception:
            session.rollback()
        finally:
            session.close()

    @staticmethod
    def find() -> List[User]:
        try:
            with session.begin():
                users = session.query(User)
                
                users_list = []

                for user in users:
                    users_list.append(user.to_dict())
            return users_list
        except:
            session.rollback()
        finally:
            session.close()
            
    @staticmethod
    def find_by_id(id_: str) -> UserResponseDTO:
        try:
            with session.begin():
                user = session.query(User).filter(User.id_ == id_).first()

            return user.to_dict()
        except:
            session.rollback()
        finally:
            session.close()

    @staticmethod
    def find_by_mail(mail: str) -> UserResponseDTO:
        try:
            with session.begin():
                user = session.query(User).filter(User.mail == mail).first()

            return user.to_dict()
        except:
            session.rollback()
        finally:
            session.close()

    @staticmethod
    def get_user_password(id_: str) -> UserPasswordResponseDTO:
        try:
            with session.begin():
                user_password = session.query(User).filter(User.id_ == id_).first().password

            return user_password
        except:
            session.rollback()
        finally:
            session.close()

    @staticmethod
    def update(id_: str, data: UserUpdateDTO) -> None:
        try:
            with session.begin():
                session.query(User).filter(User.id_==id_).update(data)
        except:
            session.rollback()
        finally:
            session.close()

    @staticmethod
    def delete(id_: str) -> None:
        try:
            with session.begin():
                session.query(User).filter(User.id_==id_).delete()
        except:
            session.rollback()
        finally:
            session.close()