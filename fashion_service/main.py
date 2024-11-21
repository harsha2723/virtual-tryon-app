from fastapi import FastAPI, UploadFile, BackgroundTasks
from pydantic import BaseModel
import asyncio
from models import FashionItemDocument
from beanie import init_beanie
import motor.motor_asyncio

app = FastAPI()

# Example Pydantic model with updated config
class MyModel(BaseModel):
    name: str

    class Config:
        json_schema_extra = {
            "example": {"name": "Alice"}
        }

# Use lifespan event handlers instead of @app.on_event
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("App is starting")
    # Your startup logic
    yield
    print("App is shutting down")
    # Your shutdown logic

app.router.lifespan_context = lifespan

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
