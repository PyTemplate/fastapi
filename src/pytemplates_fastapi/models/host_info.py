import os
import socket

from pydantic import BaseModel


class HostInfo(BaseModel):
    host_name: str = socket.gethostname()
    host_ip: str = socket.gethostbyname(socket.gethostname())
    process_id: int = os.getpid()
