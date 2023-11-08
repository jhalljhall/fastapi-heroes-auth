from fastapi import FastAPI
from models import Hero, Ability, AbilityType, Relationship, RelationshipType
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select
from enum import Enum

from routes import heroes

app = FastAPI()
app.include_router(heroes.router)

@app.get("/")
async def root():
    return {"msg": "Hello World"}


origins = [
    "http://8000-coachhallso-fastapidock-5fztzl33j5c.ws-us106.gitpod.io",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    print(f"{repr(exc)}")
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)