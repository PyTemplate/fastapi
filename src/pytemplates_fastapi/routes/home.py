import os
import socket

from fastapi import APIRouter

from pytemplates_fastapi import models

router = APIRouter()


@router.get("/", response_model=str)
def root() -> str:
    """Display the homepage message."""
    return "Hello PyTemplates User!"


@router.get("/whoami", response_model=models.HostInfo)
def whoami() -> models.HostInfo:
    """Display the host name, host ip, and process ID which processed the request."""
    return models.HostInfo(
        host_name=socket.gethostname(),
        host_ip=socket.gethostbyname(socket.gethostname()),
        process_id=os.getpid(),
    )
