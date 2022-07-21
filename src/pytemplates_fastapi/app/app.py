from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pytemplates_fastapi.db.session import session

app = FastAPI()
# app.router.redirect_slashes = False

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event():
    print("Starting up")
    session.connect_db()


@app.on_event("shutdown")
def shutdown_event():
    print("Shutting down")
    session.close_connections()
