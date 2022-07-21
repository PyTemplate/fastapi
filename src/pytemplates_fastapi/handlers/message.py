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
            next_id_number = 1

        message = models.Message(
            id_number=next_id_number,
            content=content,
            last_updated=datetime.utcnow().isoformat(),
        )
        self.session.db[message.id_number] = message

    def read(self, id_number: int):
        message = models.Message.parse_obj(self.session.db[id_number])
        return message

    def read_all(self):
        messages = [models.Message.parse_obj(v) for v in self.session.db.values()]
        return messages

    def update(self, id_number: int, content: str):
        self.session.db[id_number].content = content

    def delete(self, id_number: int):
        del self.session.db[id_number]
