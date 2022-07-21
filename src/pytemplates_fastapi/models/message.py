from pydantic import BaseModel


class Message(BaseModel):
    id_number: int
    content: str
    last_updated: str
