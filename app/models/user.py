from pydantic import BaseModel

class UserIn(BaseModel):
    email: str
    full_name: str
    password: str

class UserOut(BaseModel):
    id: int
    email: str
    full_name: str