from cerberus import Validator
from src.utils.http_request import HttpRequest

class UserSessionValidator:
    def validator(self, data: HttpRequest) -> None:
        request_validator = Validator({
            "name": { "type": "string", "required": True, "empty": False },
            "password": { "type": "string", "required": True, "empty": False }
        })
        response = request_validator.validate(data.body)

        if response is False:
            raise Exception(request_validator.errors)