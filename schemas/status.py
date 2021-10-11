from pydantic import BaseModel


class Status(BaseModel):
    status_type: str
    message: str
