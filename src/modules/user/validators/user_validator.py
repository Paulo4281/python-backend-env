from cerberus import Validator
from src.utils.http_request import HttpRequest

class UserValidator:
    @staticmethod
    def user_auth_dto_validator(data: HttpRequest) -> None:
        user_auth_validator = Validator({
            "mail": { "type": "string", "required": True, "empty": False },
            "password": { "type": "string", "required": True, "empty": False }
        })
        response = user_auth_validator.validate(data.body)

        if response is False:
            raise Exception(user_auth_validator.errors)
        
    @staticmethod
    def user_dto_validator(data: HttpRequest) -> None:
        user_dto_validator = Validator({
            "name": { "type": "string", "required": True, "empty": False },
            "mail": { "type": "string", "required": False, "empty": True },
            "password": { "type": "string", "required": True, "empty": False },
            "age": { "type": "integer", "required": False, "empty": True }
        })
        response = user_dto_validator.validate(data.body)

        if response is False:
            raise Exception(user_dto_validator.errors)