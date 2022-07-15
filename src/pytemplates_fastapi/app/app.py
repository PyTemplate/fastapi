from fastapi import FastAPI
from pytemplates_fastapi.db.session import session

app = FastAPI()


@app.on_event("startup")
def startup_event():
    print("Starting up")
    session.connect_db()


@app.on_event("shutdown")
def shutdown_event():
    print("Shutting down")
    session.close_connections()
