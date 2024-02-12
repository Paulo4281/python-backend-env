from src.modules.user_session.services.user_session_service import UserSessionService
from flask import Response, jsonify

class UserSessionController:
    def auth() -> Response:
        data = UserSessionService.auth()
        return jsonify(data)