from typing import TypedDict
from datetime import date, datetime

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

class UserResponseDTO(UserDTO):
    id_: str
    updated_at: datetime
    created_at: datetime

class UserPasswordResponseDTO(TypedDict):
    password: str

class UserUpdateDTO(UserDTO):
    pass