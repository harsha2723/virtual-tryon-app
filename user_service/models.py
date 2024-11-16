from beanie import Document
from pydantic import BaseModel, EmailStr

class User(Document):
    email: EmailStr
    name: str
    measurements: dict

    class Settings:
        collection = "users"

class UserCreate(BaseModel):
    email: EmailStr
    name: str
    measurements: dict
