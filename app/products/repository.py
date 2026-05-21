from sqlalchemy.orm import Session
from app.products.models import Product


# Repository de produtos, responsável por interagir com o banco de dados para operações relacionadas a produtos.

# Função para recuperar todos os produtos ativos do banco de dados.
def get_all_products(db: Session, offset: int = 0, limit: int = 10) -> tuple[list[Product], int]:
    ''' Recupera todos os produtos do banco de dados. '''

    # Query base filtrando apenas produtos ativos
    query = db.query(Product).filter(Product.is_active == True)

    # Conta o total de produtos ativos para fins de paginação
    total = query.count()

    # Produtos da página atual usando offset e limit para paginação
    products = query.offset(offset).limit(limit).all()
    return products, total

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

# Função para deletar um produto do banco de dados. Na verdade, marca o produto como inativo para manter o histórico.
def delete_product(db: Session, product: Product) -> None:
   
    ''' Deleta um produto do banco de dados. '''
    
    product.is_active = False
    db.commit()
        