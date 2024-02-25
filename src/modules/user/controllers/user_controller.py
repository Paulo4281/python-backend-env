from src.modules.user.services.user_service import UserService
from src.utils.http_request import HttpRequest
from src.utils.http_response import HttpResponse
from src.utils.app_error import AppError
from src.modules.user.validators.user_validator import UserValidator
from flask import jsonify, request

class UserController:
    @staticmethod
    def auth() -> HttpResponse:
        try:
            req = HttpRequest(body=request.json)
            UserValidator().user_auth_dto_validator(req)
            service = UserService()
            response = HttpResponse(body=service.auth(req.body), status_code=200)
        except Exception as e:
            response = AppError(body=e, status_code=400).error
        return jsonify(response.body), response.status_code
    
    @staticmethod
    def save() -> HttpResponse:
        try:
            req = HttpRequest(body=request.json)
            UserValidator().user_dto_validator(req)
            service = UserService()
            response = HttpResponse(body=service.save(req.body), status_code=201)
        except Exception as e:
            response = AppError(body=e, status_code=400).error
        return jsonify(response.body), response.status_code
    
    @staticmethod
    def find() -> HttpResponse:
        try:
            service = UserService()
            response = HttpResponse(body=service.find(), status_code=200)
        except Exception as e:
            response = AppError(body=e, status_code=400).error
        return jsonify(response.body), response.status_code
    
    @staticmethod
    def find_by_id(id_: str) -> HttpResponse:
        try:
            req = HttpRequest(params=id_)
            service = UserService()
            response = HttpResponse(body=service.find_by_id(req.params), status_code=200)
        except Exception as e:
            response = AppError(body=e, status_code=400).error
        return jsonify(response.body), response.status_code
    
    @staticmethod
    def update(id_: str) -> HttpResponse:
        try:
            req = HttpRequest(params=id_, body=request.json)
            UserValidator().user_dto_validator(req)
            service = UserService()
            response = HttpResponse(body=service.update(req.params, req.body), status_code=204)
        except Exception as e:
            response = AppError(body=e, status_code=400).error
        return jsonify(response.body), response.status_code
    
    @staticmethod
    def delete(id_: str) -> HttpResponse:
        try:
            req = HttpRequest(params=id_)
            service = UserService()
            response = HttpResponse(body=service.delete(req.params), status_code=204)
        except Exception as e:
            response = AppError(body=e, status_code=400).error
        return jsonify(response.body), response.status_code