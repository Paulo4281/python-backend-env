from cerberus import Validator
from src.utils.http_request import HttpRequest
from src.utils.api_data_validator import ApiDataValidator

class BookValidator:
    @staticmethod
    def book_dto_validator(data: HttpRequest) -> None:
        book_dto_validator = Validator({
            "title": {"type": "string", "required": True, "empty": False},
            "price": {"type": "float", "required": True, "empty": False, "min": 0.01},
            "category_id": {"type": "string", "required": True, "empty": False},
            "owner_id": {"type": "string", "required": True, "empty": False}
        })
        try:
            ApiDataValidator(book_dto_validator, data.body)
        except Exception as e:
            raise Exception(e)