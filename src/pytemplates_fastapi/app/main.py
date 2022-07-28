from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pytemplates_fastapi.app.router import router
from pytemplates_fastapi.db.session import session

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://localhost",
    "https://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.on_event("startup")
def startup_event() -> None:
    print("Starting up")
    session.connect_db()


@app.on_event("shutdown")
def shutdown_event() -> None:
    print("Shutting down")
    session.close_connections()
