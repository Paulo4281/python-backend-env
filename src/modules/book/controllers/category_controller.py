from src.utils.http_request import HttpRequest
from src.utils.http_response import HttpResponse
from src.modules.book.validators.category_validator import CategoryValidator
from src.modules.book.services.category_service import CategoryService
from src.utils.app_error import AppError
from flask import jsonify, request

class CategoryController:
    @staticmethod
    def save() -> HttpResponse:
        try:
            req = HttpRequest(body=request.json)
            CategoryValidator().category_dto_validator(req)
            service = CategoryService()
            response = HttpResponse(body=service.save(req.body), status_code=200)
        except Exception as e:
            response = AppError(body=e, status_code=400)
        return jsonify(response.body), response.status_code
        