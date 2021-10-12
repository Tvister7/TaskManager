import uvicorn
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from endpoints import hello, users, token, tasks

app = FastAPI(title="AuthProject")

app.include_router(hello.router, prefix="/hello", tags=["hello"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(token.router, prefix="/token", tags=["token"])
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])


register_tortoise(
    app,
    db_url="sqlite://user_task.db",
    modules={"models": ["models.tasks", "models.users"]},
    generate_schemas=True,
    add_exception_handlers=True
)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="127.0.0.1", reload=True)
