from pydantic import BaseModel


class Message(BaseModel):
    id_number: int
    content: str
    timestamp: str
