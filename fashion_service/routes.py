from fastapi import APIRouter, BackgroundTasks
from pydantic import BaseModel

router = APIRouter()

class TryOnRequest(BaseModel):
    email: str
    item_id: str

async def send_notification(email: str):
    print(f"Sending notification to {email}")

@router.post("/try-on")
async def try_on(request: TryOnRequest, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_notification, request.email)
    return {"msg": "Try-on successful"}
    