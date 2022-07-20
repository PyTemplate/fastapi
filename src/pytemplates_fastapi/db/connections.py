import json
import os
from pathlib import Path
from typing import Dict


class ConnectionHandler:
    """Handle all database connections throughout the API."""

    def __init__(self) -> None:
        print("Initializing Session")
        self.filename = os.path.join(str(Path(__file__).parent), "mock_database.json")
        self.db: Dict = {}

    def connect_db(self):
        print("Connecting")
        if os.path.getsize(self.filename) != 0:
            with open(self.filename, "r", encoding="UTF-8") as f:
                data = json.load(f)
                int_keys = [int(k) for k in data.keys()]
                db = dict(zip(int_keys, data.values()))
                self.db = db
        print(self.db)

    def close_connections(self):
        print("Disconnecting")
        with open(self.filename, "w", encoding="UTF-8") as f:
            json.dump(self.db, f)
