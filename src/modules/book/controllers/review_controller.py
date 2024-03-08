from src.utils.http_response import HttpResponse
from src.utils.http_request import HttpRequest
from src.utils.app_error import AppError
from src.modules.book.validators.review_validator import ReviewValidator
from src.modules.book.services.review_service import ReviewService
from flask import jsonify, request

class ReviewController:
    @staticmethod
    def save() -> HttpResponse:
        try:
            req = HttpRequest(body=request.json)
            ReviewValidator().review_dto_validator(req)
            service = ReviewService()
            response = HttpResponse(body=service.save(req.body), status_code=201)
        except Exception as e:
            response = AppError(body=e, status_code=400).error
        return jsonify(response.body), response.status_code