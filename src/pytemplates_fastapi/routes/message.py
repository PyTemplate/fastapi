from typing import List, Optional

from fastapi import APIRouter, Body, HTTPException, status
from pytemplates_fastapi import handlers, models

router = APIRouter()
message_handler = handlers.MessageHandler()


@router.post(
    "/create", status_code=status.HTTP_201_CREATED, response_model=models.HTTPResponse
)
def create_message(content: str = Body(embed=True)) -> models.HTTPResponse:
    message_handler.create(content=content)
    response = models.HTTPResponse(status="CREATED")
    return response


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=List[models.Message],
    responses={404: {"description": "Not Found", "model": models.HTTPError}},
)
def read_messages(id_number: Optional[int] = None) -> List[models.Message]:
    """Read the messages from the db. Optionally filter by id_number."""

    if id_number:
        try:
            messages = [message_handler.read(id_number=id_number)]
        except KeyError:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="id_number not found"
            ) from None
    else:
        messages = message_handler.read_all()
    return messages


@router.put(
    "/update/{id_number}",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=models.HTTPResponse,
    responses={404: {"description": "Not Found", "model": models.HTTPError}},
)
def update_message(
    id_number: int, content: str = Body(embed=True)
) -> models.HTTPResponse:
    """Update a message in the db."""

    try:
        message_handler.update(id_number=id_number, content=content)
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="id_number not found"
        ) from None

    response = models.HTTPResponse(status="UPDATED")

    return response


@router.delete(
    "/delete/{id_number}",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=models.HTTPResponse,
    responses={404: {"description": "Not Found", "model": models.HTTPError}},
)
def delete_message(id_number: int) -> models.HTTPResponse:
    "Delete a message from the db."

    try:
        message_handler.delete(id_number=id_number)
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="id_number not found"
        ) from None

    response = models.HTTPResponse(status="DELETED")

    return response
