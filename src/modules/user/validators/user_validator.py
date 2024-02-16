from cerberus import Validator
from src.utils.http_request import HttpRequest
from src.utils.api_data_validator import ApiDataValidator

class UserValidator:
    @staticmethod
    def user_auth_dto_validator(data: HttpRequest) -> None:
        user_auth_dto_validator = Validator({
            "mail": { "type": "string", "required": True, "empty": False },
            "password": { "type": "string", "required": True, "empty": False }
        })
        try:
            ApiDataValidator(user_auth_dto_validator, data.body)
        except Exception as e:
            raise Exception(e)
        
    @staticmethod
    def user_dto_validator(data: HttpRequest) -> None:
        user_dto_validator = Validator({
            "name": { "type": "string", "required": True, "empty": False },
            "mail": { "type": "string", "required": False, "empty": True },
            "password": { "type": "string", "required": True, "empty": False },
            "age": { "type": "integer", "required": False, "empty": True }
        })
        try:
            ApiDataValidator(user_dto_validator, data.body)
        except Exception as e:
            raise Exception(e)