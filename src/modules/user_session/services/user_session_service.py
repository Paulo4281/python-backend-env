from src.modules.user_session.dtos.user_session_dto import UserSessionDTO
class UserSessionService:
    def auth(data: UserSessionDTO) -> any:
        return {
            "name": data["name"],
            "password": data["password"]
        }