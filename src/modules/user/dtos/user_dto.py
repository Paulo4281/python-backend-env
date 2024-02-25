from typing import TypedDict
from datetime import date

class UserAuthDTO(TypedDict):
    mail: str
    password: str

class UserAuthResponseDTO(TypedDict):
    name: str
    mail: str
    birth: date
    message: str

class UserDTO(TypedDict):
    name: str
    mail: str
    password: str
    birth: date

class UserResponseDTO(TypedDict):
    id_: str
    name: str
    mail: str
    password: str
    birth: date
    created_at: str

class UserUpdateDTO(UserDTO):
    pass