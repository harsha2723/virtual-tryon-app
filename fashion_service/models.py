from pydantic import BaseModel, Field
from beanie import Document, PydanticObjectId
from typing import List

# Pydantic schema for fashion items
class FashionItem(BaseModel):
    name: str
    category: str
    image_url: str
    size: str
    price: float

    class Config:
        schema_extra = {
            "example": {
                "name": "T-Shirt",
                "category": "Clothing",
                "image_url": "https://example.com/tshirt.jpg",
                "size": "M",
                "price": 19.99
            }
        }

# Beanie model for MongoDB (MongoDB Document)
class FashionItemDocument(FashionItem, Document):
    pass
