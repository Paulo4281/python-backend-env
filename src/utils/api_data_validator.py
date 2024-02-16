from cerberus import Validator
from typing import Any

class ApiDataValidator():
    def __init__(self, validator: Validator, data: Any) -> None:
        self.validator = validator
        self.data = data
        self.__validate()

    def __validate(self) -> bool:
        api_data_validator = self.validator.validate(self.data)
        if api_data_validator is False:
            raise Exception(self.validator.errors)
        return True