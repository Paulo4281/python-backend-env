from typing import TypedDict
from datetime import datetime

class AuthorDTO(TypedDict):
    name: str
    birth: str
    death: str
    nationality: str

class AuthorResponseDTO(TypedDict):
    id_: str
    name: str
    birth: str
    death: str
    nationality: str
    updated_at: datetime
    created_at: datetime

class AuthorUpdateDTO(AuthorDTO):
    pass