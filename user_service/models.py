from pydantic import BaseModel, EmailStr
from beanie import Document

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john.doe@example.com",
                "password": "securepassword123"
            }
        }

class UserDocument(UserCreate, Document):
    pass
