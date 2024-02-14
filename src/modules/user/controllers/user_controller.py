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
            response = HttpResponse(body=UserService.auth(req.body), status_code=200)
        except Exception as exception:
            response = AppError(body=exception, status_code=400).error
        return jsonify(response.body), response.status_code
    
    @staticmethod
    def save() -> HttpResponse:
        try:
            req = HttpRequest(body=request.json)
            UserValidator().user_dto_validator(req)
            response = HttpResponse(body=UserService.save(req.body), status_code=200)
        except Exception as exception:
            response = AppError(body=exception, status_code=400).error
        return jsonify(response.body), response.status_code
    
    @staticmethod
    def find() -> HttpResponse:
        try:
            response = HttpResponse(body=UserService.find(), status_code=200)
        except Exception as exception:
            response = AppError(body=exception, status_code=400).error
        return jsonify(response.body), response.status_code
    
    @staticmethod
    def find_by_id(id: str) -> HttpResponse:
        try:
            req = HttpRequest(params=id)
            response = HttpResponse(body=UserService.find_by_id(req.params), status_code=200)
        except Exception as exception:
            response = AppError(body=exception, status_code=400).error
        return jsonify(response.body), response.status_code
    
    @staticmethod
    def update(id: str) -> HttpResponse:
        try:
            req = HttpRequest(params=id, body=request.json)
            UserValidator().user_dto_validator(req)
            response = HttpResponse(body=UserService.update(req.params, req.body), status_code=200)
        except Exception as exception:
            response = AppError(body=exception, status_code=400).error
        return jsonify(response.body), response.status_code
    
    @staticmethod
    def delete(id: str) -> HttpResponse:
        try:
            req = HttpRequest(params=id)
            response = HttpResponse(body=UserService.delete(req.params), status_code=200)
        except Exception as exception:
            response = AppError(body=exception, status_code=400).error
        return jsonify(response.body), response.status_code