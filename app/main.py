from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import api

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins={"*"},
    allow_credentials=True,
    allow_methods={"OPTION", "GET", "POST"},
    allow_headers={"*"},
)


@app.on_event("startup")
async def startup_event():
    from app.config import settings
    from app.database import Base, engine, get_db

    session = next(get_db())
    try:
        session.execute(f"CREATE DATABASE IF NOT EXISTS {settings.DB_NAME};")
    finally:
        session.close()

    Base.metadata.create_all(bind=engine)


@app.get("/")
async def healthcheck():
    return {"ok": "True"}


app.include_router(api.router)
