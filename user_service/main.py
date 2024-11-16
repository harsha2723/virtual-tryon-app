from fastapi import FastAPI, HTTPException
from models import UserCreate, UserDocument
from beanie import init_beanie
import motor.motor_asyncio

app = FastAPI()

# MongoDB client setup
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://mongo:27017")
db = client.virtual_try_on_db

# Startup event to initialize the database
@app.on_event("startup")
async def start_db():
    await init_beanie(database=db, document_models=[UserDocument])

@app.post("/register")
async def register_user(user: UserCreate):
    existing_user = await UserDocument.find_one(UserDocument.email == user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    new_user = UserDocument(**user.dict())
    await new_user.insert()
    return {"msg": "User registered successfully"}
