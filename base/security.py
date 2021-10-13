import os
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from passlib.context import CryptContext
from schemas.user_schema import User_Pydantic

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))

SECRET_KEY = os.environ["SECRET_KEY"]
ALGORITHM = os.environ["ALGORITHM"]
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ["ACCESS_TOKEN_EXPIRE_MINUTES"])

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/token/')


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return password_context.hash(password)


def make_token(user_obj: User_Pydantic, secret_key: str = SECRET_KEY, algorithm: str = ALGORITHM):
    return jwt.encode(user_obj.dict(), secret_key, algorithm=algorithm)
