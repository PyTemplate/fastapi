import json
import os
from pathlib import Path
from typing import Dict

from pytemplates_fastapi import models


class ConnectionHandler:
    """Handle all database connections throughout the API."""

    def __init__(self) -> None:
        print("Initializing Session")
        self.filename = os.path.join(str(Path(__file__).parent), "mock_database.json")
        self.db: Dict[int, models.Message] = {}

    def connect_db(self):
        print("Connecting")
        if os.path.getsize(self.filename) != 0:
            with open(self.filename, "r", encoding="UTF-8") as f:
                data = json.load(f)
                int_keys = [int(k) for k in data.keys()]
                messages = [models.Message.parse_obj(v) for v in data.values()]
                db = dict(zip(int_keys, messages))
                self.db = db
        print(self.db)

    def close_connections(self):
        print("Disconnecting")
        with open(self.filename, "w", encoding="UTF-8") as f:
            data = [v.dict() for v in self.db.values()]
            db = dict(zip(self.db.keys(), data))
            json.dump(db, f)
            f.write("\n")
