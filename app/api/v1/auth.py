from app.api.deps import verify_telegram_login
from fastapi import APIRouter, Depends

router = APIRouter()


@router.post("")
async def verfiy_telegram(token: str = Depends(verify_telegram_login)):
    return {"token": token}
