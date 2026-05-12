from pydantic import BaseModel
from typing import Optional

# Schemas para criação de produtos, incluindo campos como nome, descrição, preço e estoque.
class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int = 0

# Schema para resposta de produto, incluindo o ID gerado pelo banco de dados e o status de atividade.
class ProductResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    stock: int
    is_active: bool

    class Config:
        from_attributes = True