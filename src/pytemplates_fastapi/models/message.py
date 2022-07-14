from datetime import datetime

from pydantic import BaseModel


class Message(BaseModel):
    id: int
    content: str
    timestamp: str = datetime.utcnow().isoformat()
