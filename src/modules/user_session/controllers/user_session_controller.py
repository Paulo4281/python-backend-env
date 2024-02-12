from src.modules.user_session.services.user_session_service import UserSessionService
from src.utils.http_request import HttpRequest
from src.utils.http_response import HttpResponse
from src.utils.app_error import AppError
from src.modules.user_session.validators.user_session_validator import UserSessionValidator
from flask import jsonify, request

class UserSessionController:
    def auth() -> HttpResponse:
        try:
            data = HttpRequest(body=request.json)
            UserSessionValidator().validator(data)
            response = HttpResponse(body=UserSessionService.auth(data.body), status_code=200)
        except Exception as exception:
            response = AppError(body=exception, status_code=400).error
        return jsonify(response.body), response.status_code