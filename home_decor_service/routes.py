from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class RoomScanRequest(BaseModel):
    email: str
    room_data: dict

@router.post("/scan-room")
async def scan_room(request: RoomScanRequest):
    return {"msg": "Room scan saved", "data": request.room_data}
