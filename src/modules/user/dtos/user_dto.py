from typing import TypedDict

class UserAuthDTO(TypedDict):
    name: str
    password: str

class UserDTO(TypedDict):
    name: str
    mail: str
    password: str
    age: int