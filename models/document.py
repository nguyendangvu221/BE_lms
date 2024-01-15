from pydantic import BaseModel
from datetime import datetime
class Document(BaseModel):
    name: str
    author: str
    idPoster: str
    category: str
    publisher: str
    description: str
    numberOfPage: int
    reprint: int
    numberOfEditions: int
    language: str
    releaseDate: datetime
    image: str
    pdf: str
    namePoster: str