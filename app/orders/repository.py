from sqlalchemy.orm import Session

from app.orders.models import Order, OrderItem

# Funções de repositório para manipular os pedidos e itens de pedido no banco de dados.

# Função para criar um novo pedido no banco de dados.
def create_order(db: Session, user_id: int, status: str, total: float) -> Order:
    """Cria um novo pedido no banco de dados."""
    new_order = Order(user_id=user_id, status="Pendente", total=total)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

# Função para criar um novo item de pedido no banco de dados.
def create_order_item(db: Session, order_id: int, product_id: int, quantity: int, price: float) -> OrderItem:
    """Cria um novo item de pedido no banco de dados."""
    new_item = OrderItem(order_id=order_id, product_id=product_id, quantity=quantity, price=price)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

# Função para recuperar todos os pedidos de um usuário específico.
def get_orders_by_user(db: Session, user_id: int) -> list[Order]:
    """Recupera todos os pedidos de um usuário específico."""
    return db.query(Order).filter(Order.user_id == user_id).order_by(Order.created_at.desc()).all()

# Função para recuperar um pedido específico pelo ID.
def get_order_by_id(db: Session, order_id: int) -> Order:
    """Recupera um pedido específico pelo ID."""
    return db.query(Order).filter(Order.id == order_id).first()