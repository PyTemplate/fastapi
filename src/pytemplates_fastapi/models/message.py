from pydantic import BaseModel, Field

from pytemplates_fastapi import models


class Message(BaseModel):
    id_number: int = Field(
        description="Unique ID for the message.",
        example=1,
        gt=0,
    )
    content: str = Field(
        description="Content of the message.", example="Hello PyTemplates User!"
    )
    last_updated: str = Field(
        description="An ISO formatted datetime string.",
        example="2022-07-30T23:58:26.997075",
    )


class MessageCreated(models.HTTPResponse, Message):
    status = models.Status("CREATED")


class MessageUpdated(models.HTTPResponse, Message):
    status = models.Status("UPDATED")
    content: str = Field(
        description="New content of the message.",
        example="Hello Again PyTemplates User!",
    )


class MessageDeleted(models.HTTPResponse):
    status = models.Status("DELETED")
    id_number: int = Field(
        description="Unique ID for the message.",
        example=1,
        gt=0,
    )
