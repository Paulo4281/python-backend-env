from src.modules.user.entities.user import User
from src.modules.user.dtos.user_dto import UserDTO
from src.database.database_config import session
from uuid import uuid4
import datetime

class UserRepository:
    def save(self, data: UserDTO) -> User:
        try:
            user = User(
                    id = uuid4(),
                    name = data["name"],
                    mail = data["mail"],
                    password = data["password"],
                    age = data["age"],
                    created_at = datetime.datetime.now()
            )

            session.add(user)
            session.commit()

            return user.toDict()
        except Exception as exception:
            session.rollback()
            raise Exception(exception)
        finally:
            session.close()