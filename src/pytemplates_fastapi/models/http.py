from enum import Enum

from pydantic import BaseModel


class Status(str, Enum):
    CREATED = "CREATED"
    UPDATED = "UPDATED"
    DELETED = "DELETED"


class HTTPResponse(BaseModel):
    status: Status


class HTTPError(BaseModel):
    detail: str
