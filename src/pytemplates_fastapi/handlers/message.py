from datetime import datetime

from pytemplates_fastapi import models
from pytemplates_fastapi.db.session import session


class MessageHandler:
    """Handle CRUD operations for models.Message resources."""

    def __init__(self) -> None:
        self.session = session

    def create(self, content: str):
        """Create a new models.Message and store it in the db."""
        if self.session.db:
            next_id_number = max(self.session.db.keys()) + 1
        else:
            next_id_number = 0
        message = models.Message(
            id_number=next_id_number,
            content=content,
            timestamp=datetime.utcnow().isoformat(),
        )
        self.session.db[message.id_number] = message.dict()
        return f"Created message with ID: {message.id_number}"

    def read(self, id_number: int):
        message = models.Message.parse_obj(self.session.db[id_number])
        return message

    def read_all(self):
        messages = [models.Message.parse_obj(v) for v in self.session.db.values()]
        return messages

    def update(self, id_number: int, content: str):
        message = models.Message(
            id_number=id_number,
            content=content,
            timestamp=datetime.utcnow().isoformat(),
        )
        self.session.db[id_number] = message.dict()
        return message

    def delete(self, id_number: int):
        del self.session.db[id_number]
        return f"Deleted message with id_number: {id_number}"
