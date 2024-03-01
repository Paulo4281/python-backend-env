from cerberus import Validator
from src.utils.http_request import HttpRequest
from src.utils.api_data_validator import ApiDataValidator

class AuthorValidator:
    @staticmethod
    def author_dto_validator(data: HttpRequest) -> None:
        author_dto_validator = Validator({
        "name": { "type": "string", "required": True, "empty": False },
        "birth": { "type": "string", "required": True, "empty": True },
        "death": { "type": "string", "required": True, "empty": True },
        "nationality": { "type": "string", "required": True, "empty": False }
        })
        try:
            ApiDataValidator(author_dto_validator, data.body)
        except Exception as e:
            raise Exception(e)