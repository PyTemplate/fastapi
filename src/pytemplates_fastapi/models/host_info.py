from pydantic import BaseModel


class HostInfo(BaseModel):
    host_name: str
    host_ip: str
    process_id: int
