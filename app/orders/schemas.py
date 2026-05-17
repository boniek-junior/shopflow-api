from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from app.products.schemas import ProductResponse

# Schemas para pedidos
class OrderItemResponse(BaseModel):
    id: int
    quantity: int
    price: float
    product: ProductResponse

    class Config:
        orm_mode = True

# Schemas para pedidos
class OrderResponse(BaseModel):
    id: int
    status: str
    total: float
    created_at: datetime
    items: list[OrderItemResponse]

    class Config:
        orm_mode = True