from pydantic import BaseModel, Field


class HostInfo(BaseModel):
    host_name: str = Field(
        description="Name of the host machine processing the request.", example="ubuntu"
    )
    host_ip: str = Field(
        description="IP address of the host machine processing the request.",
        example="127.0.0.1",
    )
    process_id: int = Field(description="Process ID processing the request.")
