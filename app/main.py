from typing import Union
import time
from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.routers.auth import router as auth_router
from app.routers.question import router as question_router
from app.routers.option import router as option_router
from app.routers.topic import router as topic_router
from app.routers.game import router as game_router

from app.admin import admin
# from starlette.routing import Mount
from starlette.applications import Starlette


app = FastAPI()

app.include_router(auth_router)
app.include_router(question_router)
app.include_router(option_router)
app.include_router(topic_router)
app.include_router(game_router)

admin.mount_to(app)

@app.get("/")
async def root():
    return {
        "GitHub Repository": "https://github.com/globallstudent/bilimdon_clone",
        "Swagger Docs": "Go to https://globalstudent-bilimdon.loca.lt/docs to see API docs",
        "Admin Panel": "Go to /admin to access Starlette Admin"
    }