from passlib.context import CryptContext
from jose import JWTError, jwt

password = "paswword123"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password):
    hashed_password = pwd_context.hash(password)
    print(password)
    print(hashed_password)

hash_password(password)


def verify(password, hashed_password):
    return pwd_context.verify(password, hash_password)


