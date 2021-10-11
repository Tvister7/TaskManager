from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def hello(name: str):
    return {"Greetings": f"Hello, {name}!"}
