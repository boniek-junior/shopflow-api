from sqlalchemy.orm import Session
from app.products.models import Product

# Repository de produtos, responsável por interagir com o banco de dados para operações relacionadas a produtos.

# Função para recuperar todos os produtos ativos do banco de dados.
def get_all_products(db: Session) -> list[Product]:
    ''' Recupera todos os produtos do banco de dados. '''
    return db.query(Product).filter(Product.is_active == True).all()

# Função para recuperar um produto específico do banco de dados com base no ID.
def get_product_by_id(db: Session, product_id: int) -> Product:
    ''' Recupera um produto específico do banco de dados com base no ID. '''
    return db.query(Product).filter(Product.id == product_id, Product.is_active == True).first()

# Função para criar um novo produto no banco de dados.
def create_product(db: Session, name: str, description: str, price: int, stock: int) -> Product:
    ''' Cria um novo produto no banco de dados. '''
    
    product = Product(
        name=name,
        description=description,
        price=price,
        stock=stock
    )
    
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

# Função para atualizar um produto existente no banco de dados.
def delete_product(db: Session, product_id: int) -> None:
    ''' Deleta um produto do banco de dados. '''
    
    product = db.query(Product).filter(Product.id == product_id).first()
    
    if product:
        product.is_active = False
        db.commit()
        db.refresh(product)
    
    return product