from fastapi import FastAPI
from app.routers import auth, users, topic, question, option

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(auth.router)
app.include_router(users.router)
app.include_router(topic.router)
app.include_router(question.router)
app.include_router(option.router)
