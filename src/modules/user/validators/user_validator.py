from cerberus import Validator
from src.utils.http_request import HttpRequest

class UserValidator:
    def auth_validator(self, data: HttpRequest) -> None:
        auth_validator = Validator({
            "name": { "type": "string", "required": True, "empty": False },
            "password": { "type": "string", "required": True, "empty": False }
        })
        response = auth_validator.validate(data.body)

        if response is False:
            raise Exception(auth_validator.errors)
        
    def save_validator(self, data: HttpRequest) -> None:
        save_validator = Validator({
            "name": { "type": "string", "required": True, "empty": False },
            "mail": { "type": "string", "required": False, "empty": True },
            "password": { "type": "string", "required": True, "empty": False },
            "age": { "type": "integer", "required": False, "empty": True }
        })
        response = save_validator.validate(data.body)

        if response is False:
            raise Exception(save_validator.errors)