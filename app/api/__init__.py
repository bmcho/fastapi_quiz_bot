from fastapi import APIRouter

from . import deps, v1

router = APIRouter()
router.include_router(v1.router, prefix="/v1")
