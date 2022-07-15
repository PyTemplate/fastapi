class ConnectionHandler:
    def __init__(self) -> None:
        print("Initializing")
        self.db = None
        print(self.db)

    def connect_db(self):
        print("Connecting")
        self.db = {}
        print(self.db)

    def close_connections(self):
        print("Disconnecting")
        if self.db:
            self.db = None
