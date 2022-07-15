from pytemplates_fastapi import models
from pytemplates_fastapi.db.session import session


class MessageHandler:
    def __init__(self) -> None:
        self.connection_handler = session
        self.count = 0

    def create(self, content: str):
        message = models.Message(id=self.count, content=content)
        self.connection_handler.db[message.id] = message.dict()
        self.count += 1
        return f"Created message with ID: {message.id}"

    def read(self, id: int):
        return self.connection_handler.db[id]

    def read_all(self):
        return list(self.connection_handler.db.values())

    def update(self, id: int, content: str):
        message = models.Message(id=id, content=content)
        self.connection_handler.db[id] = message.dict()
        return message

    def delete(self, id: int):
        del self.connection_handler.db[id]
        return f"Deleted message with ID: {id}"
