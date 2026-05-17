from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.orders.repository import create_order, create_order_item, get_orders_by_user, get_order_by_id
from app.cart.repository import get_cart_by_user_id, remove_item_from_cart
from app.products.repository import get_product_by_id

# Serviços para manipular a lógica de negócios relacionada aos pedidos, incluindo a criação de pedidos, adição de itens ao pedido e recuperação de pedidos.
# 1. Valida o carrinho
# 2. Valida estoque de cada produto
# 3. Cria o pedido e os itens
# 4. Desconta o estoque
# 5. Esvazia o carrinho

def checkout_service(db: Session, user_id: int):
    ''' Realiza o processo de checkout para um usuário. '''
    
    # Busca o carrinho do usuário
    cart = get_cart_by_user_id(db, user_id)

    # Valida se o carrinho existe e não está vazio
    if not cart or not cart.items:
        raise HTTPException(status_code=400, detail="Carrinho vazio")

    # Valida estoque de todos os produtos antes de criar o pedido
    for item in cart.items:
        product = get_product_by_id(db, item.product_id)

        if not product or not product.is_active:
            raise HTTPException(status_code=404, detail=f"Produto com ID {item.product_id} não encontrado")
     
        if product.stock < item.quantity:
            raise HTTPException(status_code=400, detail=f"Estoque insuficiente para o produto {product.name}")

    # Calcula o total do pedido
    total = sum(get_product_by_id(db, item.product_id).price * item.quantity for item in cart.items)

    # Cria o pedido no banco de dados
    order = create_order(db, user_id=user_id, status="Pendente", total=total)

    # Cria os itens do pedido e atualiza o estoque dos produtos no banco de dados
    for item in cart.items:
        product = get_product_by_id(db, item.product_id)
        
        # Salva o preço atual do produto no item do pedido para garantir que o valor do pedido seja consistente mesmo que o preço do produto mude posteriormente
        create_order_item(db, order_id=order.id, product_id=item.product_id, quantity=item.quantity, price=product.price)
       
        # Desconta o estoque do produto
        product.stock -= item.quantity
        db.commit()
        remove_item_from_cart(db, item)

    # Esvazia o carrinho do usuário após a criação do pedido
    for item in cart.items:
        remove_item_from_cart(db, item)

    return order

# Retoran o históricos de pedidos do usuário
def get_orders_service(db: Session, user_id: int):
    ''' Recupera todos os pedidos de um usuário específico. '''
    
    return get_orders_by_user(db, user_id)

# Retorna um pedido específico, garantindo que o pedido pertença ao usuário.
def get_order_by_id_service(db: Session, order_id: int, user_id: int):
    ''' Recupera um pedido específico pelo ID, garantindo que o pedido pertença ao usuário. '''
    
    # Valida se o pedido existe e pertence ao usuário
    order = get_order_by_id(db, order_id)

    # Valida se o pedido existe
    if not order:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    
    # Valida se o pedido pertence ao usuário autenticado
    if order.user_id != user_id:
        raise HTTPException(status_code=403, detail="Acesso negado ao pedido")

    return order