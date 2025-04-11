from fastapi import FastAPI
from app.routers import auth, users, topic, question, option

from app.admin import admin
# from starlette.routing import Mount
from starlette.applications import Starlette


app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(topic.router)
app.include_router(question.router)
app.include_router(option.router)

admin.mount_to(app)

@app.get("/")
async def root():
    return {
        "GitHub Repository": "https://github.com/globallstudent/bilimdon_clone",
        "Swagger Docs": "Go to https://globalstudent-bilimdon.loca.lt/docs to see API docs",
        "Admin Panel": "Go to /admin to access Starlette Admin"
    }