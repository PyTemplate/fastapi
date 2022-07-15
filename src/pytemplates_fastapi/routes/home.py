from fastapi import APIRouter
from pytemplates_fastapi.app import app
from pytemplates_fastapi.models.host_info import HostInfo

router = APIRouter()


@router.get("/")
def root():
    return "Hello PyTemplates User!"


@router.get("/whoami", response_model=HostInfo)
def whoami():
    return HostInfo()
