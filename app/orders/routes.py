from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.auth.dependencies import get_current_user
from app.users.models import User
from app.orders.schemas import OrderResponse
from app.orders.service import checkout_service, get_orders_service, get_order_by_id_service

# Roteador para as rotas relacionadas aos pedidos, incluindo operações para checkout, obtenção de pedidos e detalhes de um pedido específico. As rotas dependem do usuário autenticado e do banco de dados para realizar as operações necessárias.

# Roteador para rotas dos pedidos
router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)

# Endpoint para realizar o checkout do carrinho de compras do usuário autenticado. Cria um novo pedido com os itens do carrinho e retorna os detalhes do pedido criado.
@router.post("/checkout", response_model=OrderResponse)
def checkout(
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    return checkout_service(db, current_user.id)

# Endpoint para obter o histórico de pedidos do usuário autenticado. Retorna uma lista de pedidos realizados pelo usuário.
@router.get("/", response_model=list[OrderResponse])
def get_orders(
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    return get_orders_service(db, current_user.id)

# Endpoint para obter os detalhes de um pedido específico pelo ID do pedido. Garante que o pedido pertença ao usuário autenticado antes de retornar os detalhes do pedido.
@router.get("/{order_id}", response_model=OrderResponse)
def get_order(
        order_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    return get_order_by_id_service(db, order_id, current_user.id)