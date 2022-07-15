from typing import List

from fastapi import APIRouter, HTTPException, status
from pytemplates_fastapi import models
from pytemplates_fastapi.handlers import MessageHandler

router = APIRouter()
message_handler = MessageHandler()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_message(content: str) -> str:
    response = message_handler.create(content=content)
    return response


@router.get("/", status_code=status.HTTP_200_OK, response_model=models.Message)
def read_message(id: int) -> models.Message:
    try:
        message = message_handler.read(id=id)
    except KeyError:
        raise HTTPException(status_code=404, detail="id not found")

    return message


@router.get(
    "/all_messages", status_code=status.HTTP_200_OK, response_model=List[models.Message]
)
def read_messages() -> models.Message:
    messages = message_handler.read_all()
    return messages


@router.put("/", status_code=status.HTTP_202_ACCEPTED, response_model=models.Message)
def update_message(id: int, content: str) -> models.Message:
    try:
        response = message_handler.update(id=id, content=content)

    except KeyError:
        raise HTTPException(status_code=404, detail="id not found")

    return response


@router.delete("/", status_code=status.HTTP_202_ACCEPTED)
def delete_message(id: int) -> str:
    try:
        response = message_handler.delete(id=id)

    except KeyError:
        raise HTTPException(status_code=404, detail="id not found")

    return response
