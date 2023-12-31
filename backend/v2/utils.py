from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(plain_text_password: str) -> str:
    return pwd_context.hash(plain_text_password)




