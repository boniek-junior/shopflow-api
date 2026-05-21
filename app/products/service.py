from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.products.schemas import ProductCreate
from app.products.repository import (
    get_all_products,
    get_product_by_id,
    create_product,
    delete_product
)

from app.shared.exceptions import NotFoundException, BadRequestException, UnauthorizedException, ForbiddenException
from app.shared.pagination import PaginationParams, PaginatedResponse

# Serviço de produtos, responsável por implementar a lógica de negócios relacionada a produtos.

# Serviço para recuperar todos os produtos ativos do banco de dados.
def get_all_products_service(db: Session, params: PaginationParams) -> PaginatedResponse[ProductCreate]:
    
    ''' Serviço para recuperar todos os produtos ativos do banco de dados. '''
    
    products = get_all_products(db, offset=params.offset, limit=params.page_size)
    total = get_all_products_count(db)

    return PaginatedResponse(
        items=products,
        total=total,
        page=params.page,
        page_size=params.page_size,
        total_pages=(total + params.page_size - 1) // params.page_size
    )

# Serviço para recuperar um produto específico do banco de dados com base no ID.
def get_product_by_id_service(db: Session, product_id: int) -> ProductCreate:
   
    ''' Serviço para recuperar um produto específico do banco de dados com base no ID. '''
    
    product = get_product_by_id(db, product_id)
    
    if not product or not product.is_active:
        raise NotFoundException(detail="Produto não encontrado")
    return product

# Serviço para criar um novo produto no banco de dados.
def create_product_service(db: Session, product_data: ProductCreate) -> ProductCreate:
   
    ''' Serviço para criar um novo produto no banco de dados. '''
   
    return create_product(
        db,
        name=product_data.name,
        description=product_data.description,
        price=product_data.price,
        stock=product_data.stock
    )

# Serviço para deletar um produto do banco de dados.
def delete_product_service(db: Session, product_id: int) -> None:
   
   ''' Serviço para deletar um produto do banco de dados. '''
   
   product = get_product_by_id(db, product_id)
  
   if not product or not product.is_active:
        raise NotFoundException(detail="Produto não encontrado")
   
   delete_product(db, product_id)