from app.api.deps import get_user
from fastapi import APIRouter, Depends

from . import auth, quiz, user, webhook

router = APIRouter()
router.include_router(webhook.router, prefix="/webhook", dependencies=[Depends(get_user)])
# router.include_router(webhook.router, prefix="/webhook")
router.include_router(auth.router, prefix="/auth", tags=["Auth"])
router.include_router(user.router, prefix="/users", tags=["User"])
router.include_router(quiz.router, prefix="/quizzes", tags=["Quiz"])
