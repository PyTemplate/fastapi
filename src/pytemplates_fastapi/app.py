from fastapi import FastAPI
from pytemplates_fastapi.db.connections import ConnectionHandler

app = FastAPI()
connection_handler = ConnectionHandler()


@app.on_event("startup")
def startup_event():
    connection_handler.connect_db()


@app.on_event("shutdown")
def shutdown_event():
    connection_handler.close_connections()
