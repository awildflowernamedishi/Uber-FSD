from datetime import datetime
from jose import JWTError, jwt

def create_access_token(user_dict: dict):
    payload = user_dict.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload.update({"exp": expire})
    encoded_jwt = jwt.encode(payload, SECRET_KEY)
    return {"access_token":encoded_jwt, "token_type": "Bearer"}


def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email:str = payload.get('email')
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    return email
