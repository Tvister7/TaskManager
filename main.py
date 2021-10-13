import os
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_pagination import add_pagination
from endpoints import hello, users, token, tasks
from db import init_db

app = FastAPI(title="AuthProject")


@app.on_event("startup")
async def startup_event():
    init_db(app)

app.include_router(hello.router, prefix="/hello", tags=["hello"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(token.router, prefix="/token", tags=["token"])
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])

load_dotenv(".env")
HOST = os.environ["UVICORN_HOST"]
PORT = int(os.environ["UVICORN_PORT"])

add_pagination(app)

if __name__ == "__main__":
    uvicorn.run("main:app", port=PORT, host=HOST, reload=True)
