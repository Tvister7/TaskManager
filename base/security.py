from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from passlib.context import CryptContext
from schemas.user_schema import User_Pydantic

SECRET_KEY = "bdb9640a91ca4368ccfc171583da9cc87af1992c520759f5b1639ccb1f62e704"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return password_context.hash(password)


def make_token(user_obj: User_Pydantic, secret_key: str = SECRET_KEY, algorithm: str = ALGORITHM):
    print(jwt.encode(user_obj.dict(), secret_key, algorithm=algorithm))
    return jwt.encode(user_obj.dict(), secret_key, algorithm=algorithm)

