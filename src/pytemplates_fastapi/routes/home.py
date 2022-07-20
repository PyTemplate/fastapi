import os
import socket

from fastapi import APIRouter
from pytemplates_fastapi import models

router = APIRouter()


@router.get("/")
def root():
    return "Hello PyTemplates User!"


@router.get("/whoami", response_model=models.HostInfo)
def whoami():
    return models.HostInfo(
        host_name=socket.gethostname(),
        host_ip=socket.gethostbyname(socket.gethostname()),
        process_id=os.getpid(),
    )
