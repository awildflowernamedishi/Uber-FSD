from datetime import datetime
from pydantic import EmailStr,BaseModel

class UserCreateRequest(BaseModel):
    name: str
    email: EmailStr 
    password: str


class UserCreateResponse(BaseModel):
    id : str 
    name: str
    created_at: datetime