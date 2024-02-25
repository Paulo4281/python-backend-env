from typing import TypedDict
from datetime import date

class UserAuthDTO(TypedDict):
    mail: str
    password: str

class UserAuthResponseDTO(TypedDict):
    token: str

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

class UserPasswordResponseDTO(TypedDict):
    password: str

class UserUpdateDTO(UserDTO):
    pass