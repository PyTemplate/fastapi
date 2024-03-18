from fastapi import APIRouter

from pytemplates_fastapi.routes import home, messages

router = APIRouter()
router.include_router(home.router, tags=["General"])
router.include_router(messages.router, prefix="/messages", tags=["Messages"])
