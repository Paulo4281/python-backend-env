from src.modules.user.services.user_service import UserService
from src.utils.http_request import HttpRequest
from src.utils.http_response import HttpResponse
from src.utils.app_error import AppError
from src.modules.user.validators.user_validator import UserValidator
from flask import jsonify, request

class UserController:
    def auth() -> HttpResponse:
        try:
            data = HttpRequest(body=request.json)
            UserValidator().auth_validator(data)
            response = HttpResponse(body=UserService.auth(data.body), status_code=200)
        except Exception as exception:
            response = AppError(body=exception, status_code=400).error
        return jsonify(response.body), response.status_code
    
    def save() -> HttpResponse:
        try:
            data = HttpRequest(body=request.json)
            UserValidator().save_validator(data)
            response = HttpResponse(body=UserService.save(data.body), status_code=200)
        except Exception as exception:
            response = AppError(body=exception, status_code=400).error
        return jsonify(response.body), response.status_code