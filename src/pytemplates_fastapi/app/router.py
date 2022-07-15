from fastapi import APIRouter
from pytemplates_fastapi.routes import home, message

router = APIRouter()
router.include_router(home.router)
router.include_router(message.router, prefix="/message")
