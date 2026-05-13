from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.auth.dependencies import get_current_user
from app.users.models import User
from app.cart.schemas import CartResponse, AddItemRequest
from app.cart.service import (
    get_cart_service,
    add_item_to_cart_service,
    remove_item_from_cart_service
)

# Roteador para as rotas relacionadas ao carrinho de compras, incluindo operações para obter o carrinho, adicionar itens e remover itens. As rotas dependem do usuário autenticado e do banco de dados para realizar as operações necessárias.
router = APIRouter(prefix="/cart", tags=["Cart"])

# Endpoint para obter o carrinho de compras do usuário autenticado. Retorna o carrinho e seus itens.
@router.get("/", response_model=CartResponse)
def get_cart(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    ''' Endpoint para obter o carrinho de compras do usuário autenticado. '''
    
    cart = get_cart_service(db, current_user.id)
    return cart

# Endpoint para adicionar um item ao carrinho de compras do usuário autenticado. Recebe os dados do item a ser adicionado e retorna o carrinho atualizado.
@router.post("/items", response_model=CartResponse)
def add_item_to_cart(data: AddItemRequest, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    ''' Endpoint para adicionar um item ao carrinho de compras do usuário autenticado. '''
    
    add_item_to_cart_service(db, current_user.id, data.product_id, data.quantity)
    return get_cart_service(db, current_user.id)

# Endpoint para remover um item do carrinho de compras do usuário autenticado. Recebe o ID do produto a ser removido e retorna o carrinho atualizado.
@router.delete("/items/{product_id}", status_code=204)
def remove_item_from_cart(product_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    ''' Endpoint para remover um item do carrinho de compras do usuário autenticado. '''
    
    remove_item_from_cart_service(db, current_user.id, product_id)