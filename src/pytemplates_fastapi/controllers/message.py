from datetime import datetime
from typing import List

from pytemplates_fastapi import models
from pytemplates_fastapi.db.session import session


class MessageController:
    """Handle CRUD operations for models.Message resources."""

    def __init__(self) -> None:
        self.session = session

    @property
    def next_id_number(self) -> int:
        if self.session.db:
            next_id = max(self.session.db.keys()) + 1
        else:
            next_id = 1

        return next_id

    def create(self, content: str) -> models.Message:
        message = models.Message(
            id_number=self.next_id_number,
            content=content,
            last_updated=datetime.utcnow().isoformat(),
        )
        self.session.db[message.id_number] = message
        return message

    def read(self, id_number: int) -> models.Message:
        message = self.session.db[id_number]
        return message

    def read_all(self) -> List[models.Message]:
        messages = list(self.session.db.values())
        return messages

    def update(self, id_number: int, content: str) -> models.Message:
        self.session.db[id_number].content = content
        return self.session.db[id_number]

    def delete(self, id_number: int) -> None:
        del self.session.db[id_number]
