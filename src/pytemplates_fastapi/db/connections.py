class ConnectionHandler:
    def __init__(self) -> None:
        self.db = self.connect_db()

    def connect_db(self):
        db = {}
        return db

    def close_connections(self):
        if self.db:
            self.db = None
