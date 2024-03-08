from cerberus import Validator
from src.utils.http_request import HttpRequest
from src.utils.api_data_validator import ApiDataValidator

class ReviewValidator:
    @staticmethod
    def review_dto_validator(data: HttpRequest) -> None:
        review_dto_validator = Validator({
            "rate": {"type": "intenger", "required": True, "empty": False, "min": 0, "max": 5},
            "review": {"type": "string", "required": False, "empty": False},
            "id_user": {"type": "string", "required": True, "empty": False},
            "id_book": {"type": "string", "required": True, "empty": False}
        })
        try:
            ApiDataValidator(review_dto_validator, data.body)
        except Exception as e:
            raise Exception(e)