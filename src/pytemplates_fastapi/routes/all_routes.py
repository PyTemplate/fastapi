import os
import socket

from fastapi import APIRouter
from pytemplates_fastapi.core.module1 import greet
from pytemplates_fastapi.core.module2 import wish_farewell

router = APIRouter()


@router.get("/")
async def root():
    return greet(user="PyTemplates User")


@router.get("/hello")
async def hello(user: str):
    return greet(user=user)


@router.get("/goodbye")
async def goodbye(user: str):
    return wish_farewell(user=user)


@router.get("/whoami")
async def whoami():
    return {
        "host_name": socket.gethostname(),
        "host_ip": socket.gethostbyname(socket.gethostname()),
        "process_id": os.getpid(),
    }
