from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie, Document

MONGO_URI = "mongodb://root:password@mongodb:27017"

client = AsyncIOMotorClient(MONGO_URI)
db = client['virtual_tryon']

async def init_db():
    from models import User
    await init_beanie(database=db, document_models=[User])
