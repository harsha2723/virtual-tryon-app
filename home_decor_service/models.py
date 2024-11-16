from pydantic import BaseModel
from beanie import Document, PydanticObjectId

# Pydantic schema for home decor items
class HomeDecorItem(BaseModel):
    name: str
    category: str
    image_url: str
    dimensions: str
    price: float

    class Config:
        schema_extra = {
            "example": {
                "name": "Sofa",
                "category": "Furniture",
                "image_url": "https://example.com/sofa.jpg",
                "dimensions": "200x90x85 cm",
                "price": 499.99
            }
        }

# Beanie model for MongoDB (MongoDB Document)
class HomeDecorItemDocument(HomeDecorItem, Document):
    pass
