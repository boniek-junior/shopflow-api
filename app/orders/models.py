from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

from app.core.database import Base

# Define os modelos de pedido e item de pedido, que representam as tabelas "orders" e "order_items" no banco de dados. Cada instância dessas classes corresponde a um registro nas respectivas tabelas. O modelo de pedido inclui informações sobre o usuário, status, total e data de criação, enquanto o modelo de item de pedido inclui informações sobre o produto, quantidade e preço. Ambos os modelos possuem relacionamentos com outros modelos para facilitar consultas e operações relacionadas a pedidos.

# Modelo de pedido
class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(String, nullable=False, default="pendente")
    total = Column(Float, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    user = relationship("User", back_populates="orders")
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")

# Modelo de item do pedido
class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)

    order = relationship("Order", back_populates="items")
    product = relationship("Product")