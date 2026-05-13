from pydantic import BaseModel
from app.products.schemas import ProductResponse

# Esquema de resposta para um item do carrinho.
class CartItemResponse(BaseModel):
    ''' Esquema de resposta para um item do carrinho. '''
    
    id: int
    product: ProductResponse
    quantity: int

    class Config:
        from_attributes = True

# Esquema de resposta para o carrinho de compras.
class CartResponse(BaseModel):
    ''' Esquema de resposta para o carrinho de compras. '''
    
    id: int
    items: list[CartItemResponse]

    class Config:
        from_attributes = True

# Esquema de requisição para adicionar um item ao carrinho.
class AddItemRequest(BaseModel):
    ''' Esquema de requisição para adicionar um item ao carrinho. '''
    
    product_id: int
    quantity: int = 1