from typing import List

from fastapi import APIRouter, Body, HTTPException, Path, status

from pytemplates_fastapi import controllers, models

router = APIRouter()
message_controller = controllers.MessageController()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=models.MessageCreated,
)
def create_message(
    content: str = Body(
        description="Content of the message.", example="Hello PyTemplates User!"
    )
) -> models.MessageCreated:
    """Create a new message and store it in the db."""
    message = message_controller.create(content=content)
    response = models.MessageCreated(**message.dict())
    return response


@router.get(
    "/{id_number}",
    status_code=status.HTTP_200_OK,
    response_model=models.Message,
    responses={404: {"description": "Not Found", "model": models.NotFoundError}},
)
def read_message(
    id_number: int = Path(default=None, description="Unique ID for the message.", gt=0)
) -> models.Message:
    """Lookup a message in the db by id_number."""

    try:
        message = message_controller.read(id_number=id_number)
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="id_number not found"
        ) from None
    else:
        return message


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=List[models.Message],
    responses={404: {"description": "Not Found", "model": models.NotFoundError}},
)
def read_all_messages() -> List[models.Message]:
    """Read all messages from the db."""
    messages = message_controller.read_all()
    return messages


@router.patch(
    "/{id_number}",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=models.MessageUpdated,
    responses={404: {"description": "Not Found", "model": models.NotFoundError}},
)
def update_message(
    id_number: int = Path(description="Unique ID for the message.", gt=0),
    content: str = Body(
        description="New content of the message.",
        example="Hello Again PyTemplates User!",
    ),
) -> models.MessageUpdated:
    """Update a message in the db."""

    try:
        new_message = message_controller.update(id_number=id_number, content=content)
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="id_number not found"
        ) from None
    else:
        response = models.MessageUpdated(**new_message.dict())
        return response


@router.delete(
    "/{id_number}",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=models.MessageDeleted,
    responses={404: {"description": "Not Found", "model": models.NotFoundError}},
)
def delete_message(
    id_number: int = Path(description="Unique ID for the message.", gt=0)
) -> models.MessageDeleted:
    "Delete a message from the db."

    try:
        message_controller.delete(id_number=id_number)
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="id_number not found"
        ) from None
    else:
        response = models.MessageDeleted(id_number=id_number)
        return response
