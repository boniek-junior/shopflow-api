from sqlalchemy import Column, Integer, String

from app.core.database import Base

# Modelo de produto para o banco de dados, representando os produtos disponíveis na loja. Inclui campos como nome, descrição, preço, estoque e status de atividade.
class Product(Base):
    ''' Modelo de produto para o banco de dados. '''
    
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False, default=0)
    is_active = Column(Integer, default=True)