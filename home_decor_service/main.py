from fastapi import FastAPI
import asyncio
from models import HomeDecorItemDocument
from beanie import init_beanie
import motor.motor_asyncio

app = FastAPI()

# MongoDB client setup
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://mongo:27017")
db = client.virtual_try_on_db

# Startup event to initialize the database
@app.on_event("startup")
async def start_db():
    await init_beanie(database=db, document_models=[HomeDecorItemDocument])

# Simulating room scanning task
async def scan_room_async():
    await asyncio.sleep(3)
    return {"details": "Room scan completed with accurate measurements"}

@app.post("/scan-room")
async def scan_room():
    result = await scan_room_async()
    return {"status": "Scan completed", "details": result['details']}

@app.post("/add-home-decor-item")
async def add_home_decor_item(item: HomeDecorItemDocument):
    await item.insert()
    return {"msg": "Home decor item added successfully"}

@app.get("/get-home-decor-items")
async def get_home_decor_items():
    items = await HomeDecorItemDocument.all().to_list()
    return items