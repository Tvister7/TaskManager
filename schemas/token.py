from pydantic import BaseModel, EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str


class Login(BaseModel):
    # email: EmailStr
    username: str
    password: str


# class TokenData(BaseModel):
#     username: str | None = None
