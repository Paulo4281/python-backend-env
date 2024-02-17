from cerberus import Validator
from src.utils.http_request import HttpRequest
from src.utils.api_data_validator import ApiDataValidator

class CategoryValidator:
    @staticmethod
    def category_dto_validator(data: HttpRequest) -> None:
        category_dto_validator = Validator({
            "name": {"type": "string", "required": True, "empty": False}
        })
        try:
            ApiDataValidator(category_dto_validator, data.body)
        except Exception as e:
            raise Exception(e)