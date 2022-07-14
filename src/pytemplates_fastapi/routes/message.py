from email import message

from fastapi import APIRouter, HTTPException, status
from pytemplates_fastapi.app import connection_handler
from pytemplates_fastapi.models.message import Message

router = APIRouter(
    prefix="/message",
)
db = connection_handler.db
count = 0


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(content: str) -> str:
    global count
    global db

    message = Message(id=count, content=content)
    db[message.id] = message.dict()
    count += 1

    return f"Created message with ID: {message.id}"


@router.get("/", status_code=status.HTTP_200_OK, response_model=Message)
def read(id: int) -> message:
    global db

    if id in db:
        message = db[id]
        return message

    else:
        raise HTTPException(status_code=404, detail="id not found")


@router.put("/", status_code=status.HTTP_202_ACCEPTED, response_model=Message)
def update(id: int, content: str) -> message:
    global db

    if id in db:
        message = Message(id=id, content=content)
        db[id] = message.dict()
        return message

    else:
        raise HTTPException(status_code=404, detail="id not found")


@router.delete("/", status_code=status.HTTP_202_ACCEPTED)
def delete(id: int) -> str:
    global db

    if id in db:
        del db[id]
        return f"Deleted message with ID: {id}"

    else:
        raise HTTPException(status_code=404, detail="id not found")
