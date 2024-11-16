from fastapi import FastAPI, UploadFile, BackgroundTasks
from pydantic import BaseModel
import asyncio
from models import FashionItemDocument
from beanie import init_beanie
import motor.motor_asyncio

app = FastAPI()

# MongoDB client setup
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://mongo:27017")
db = client.virtual_try_on_db

# Startup event to initialize the database
@app.on_event("startup")
async def start_db():
    await init_beanie(database=db, document_models=[FashionItemDocument])

# Background task to simulate image processing
async def process_image(file: UploadFile):
    await asyncio.sleep(5)
    print(f"Processed image: {file.filename}")

class ImageUploadResponse(BaseModel):
    filename: str
    status: str

@app.post("/upload-item", response_model=ImageUploadResponse)
async def upload_item(file: UploadFile, background_tasks: BackgroundTasks):
    # Save the file (for demonstration purposes)
    with open(f"uploads/{file.filename}", "wb") as f:
        content = await file.read()
        f.write(content)
    
    # Add the image processing task to the background task queue
    background_tasks.add_task(process_image, file)
    return {"filename": file.filename, "status": "Processing in background"}

@app.post("/add-fashion-item")
async def add_fashion_item(item: FashionItemDocument):
    await item.insert()
    return {"msg": "Fashion item added successfully"}

@app.get("/get-fashion-items")
async def get_fashion_items():
    items = await FashionItemDocument.all().to_list()
    return items
