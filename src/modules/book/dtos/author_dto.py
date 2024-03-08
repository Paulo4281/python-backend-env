from typing import TypedDict
from datetime import datetime

class AuthorDTO(TypedDict):
    name: str
    birth: str
    death: str
    nationality: str

class AuthorResponseDTO(AuthorDTO):
    id_: str
    updated_at: datetime
    created_at: datetime