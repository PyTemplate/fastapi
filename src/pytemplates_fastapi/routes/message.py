from typing import List

from fastapi import APIRouter, HTTPException, status
from pytemplates_fastapi import handlers, models

router = APIRouter()
message_handler = handlers.MessageHandler()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_message(content: str) -> str:
    response = message_handler.create(content=content)
    return response


@router.get("/", status_code=status.HTTP_200_OK, response_model=models.Message)
def read_message(id_number: int) -> models.Message:
    try:
        message = message_handler.read(id_number=id_number)
    except KeyError:
        raise HTTPException(status_code=404, detail="id_number not found") from None

    return message


@router.get(
    "/all_messages", status_code=status.HTTP_200_OK, response_model=List[models.Message]
)
def read_messages() -> models.Message:
    messages = message_handler.read_all()
    return messages


@router.put("/", status_code=status.HTTP_202_ACCEPTED, response_model=models.Message)
def update_message(id_number: int, content: str) -> models.Message:
    try:
        response = message_handler.update(id_number=id_number, content=content)

    except KeyError:
        raise HTTPException(status_code=404, detail="id_number not found") from None

    return response


@router.delete("/", status_code=status.HTTP_202_ACCEPTED)
def delete_message(id_number: int) -> str:
    try:
        response = message_handler.delete(id_number=id_number)

    except KeyError:
        raise HTTPException(status_code=404, detail="id_number not found") from None

    return response
