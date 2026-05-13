from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base

# Modelo de carrinho de compras usando SQLAlchemy.
class Cart(Base):
    ''' Modelo de carrinho de compras. '''
    
    __tablename__ = 'carts'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True)
    
    # Relacionamento com o modelo User.
    user = relationship('User', back_populates='cart')
    
    # Relacionamento com os itens do carrinho.
    items = relationship('CartItem', back_populates='cart', cascade='all, delete-orphan')

# Modelo de item do carrinho de compras usando SQLAlchemy.
class CartItem(Base):
    ''' Modelo de item do carrinho de compras. '''
    
    __tablename__ = 'cart_items'
    
    id = Column(Integer, primary_key=True, index=True)
    cart_id = Column(Integer, ForeignKey('carts.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    
    # Relacionamento com o modelo Cart.
    cart = relationship('Cart', back_populates='items')
    
    # Relacionamento com o modelo Product.
    product = relationship('Product')