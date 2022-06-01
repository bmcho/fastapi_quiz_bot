from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app import api

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins={"https://db-quizbot.mysql.database.azure.com", "http://localhost"},
    allow_credentials=True,
    allow_methods={"OPTION", "GET", "POST"},
    allow_headers={"*"},
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.on_event("startup")
async def startup_event():
    print("event on : startup")
    from app.database import Base, engine

    Base.metadata.create_all(bind=engine)
    print("event end : startup")


@app.get("/")
async def healthcheck():
    return {"ok": "True"}


app.include_router(api.router)
