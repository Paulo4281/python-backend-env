from src.utils.http_request import HttpRequest
from src.utils.http_response import HttpResponse
from src.utils.app_error import AppError
from src.modules.book.services.book_service import BookService
from src.modules.book.validators.book_validator import BookValidator
from flask import jsonify, request

class BookController:
    @staticmethod
    def save() -> HttpResponse:
        try:
            req = HttpRequest(body=request.json)
            BookValidator().book_dto_validator(req)
            service = BookService()
            response = HttpResponse(body=service.save(req.body), status_code=200)
        except Exception as e:
            response = AppError(body=e, status_code=400)
        return jsonify(response.body), response.status_code