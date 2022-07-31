from enum import Enum

from pydantic import BaseModel, Field


class Status(str, Enum):
    CREATED = "CREATED"
    UPDATED = "UPDATED"
    DELETED = "DELETED"


class HTTPResponse(BaseModel):
    status: Status


class NotFoundError(BaseModel):
    detail: str = Field(default="id_number not found.")
