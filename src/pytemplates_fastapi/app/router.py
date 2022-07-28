from fastapi import APIRouter
from pytemplates_fastapi.routes import home, messages

router = APIRouter()
router.include_router(home.router)
router.include_router(messages.router, prefix="/messages")
