from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.products.schemas import ProductCreate, ProductResponse
from app.auth.dependencies import get_current_user
from app.users.models import User
from app.products.service import (
    get_all_products_service,
    get_product_by_id_service,
    create_product_service,
    delete_product_service
)

# Roteador para endpoints de produtos, incluindo criação, recuperação e exclusão de produtos.
router = APIRouter(
    prefix="/products",
    tags=["products"]
)

# Endpoint para recuperar todos os produtos ativos do banco de dados. Retorna uma lista de produtos.
@router.get("/", response_model=list[ProductResponse])
def get_all_products(db: Session = Depends(get_db)):
    
    ''' Endpoint para recuperar todos os produtos ativos do banco de dados. Retorna uma lista de produtos. '''
    
    return get_all_products_service(db)

# Endpoint para recuperar um produto específico do banco de dados com base no ID. Retorna os detalhes do produto.
@router.get("/{product_id}", response_model=ProductResponse)
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    
    ''' Endpoint para recuperar um produto específico do banco de dados com base no ID. Retorna os detalhes do produto. '''
    
    return get_product_by_id_service(db, product_id)

# Endpoint para criar um novo produto no banco de dados. Recebe os dados do produto, chama o serviço de criação e retorna a resposta.
@router.post("/", response_model=ProductResponse)
def create_product(
        product: ProductCreate, 
        db: Session = Depends(get_db), 
        current_user: User = Depends(get_current_user)
):
    
    ''' Endpoint para criar um novo produto no banco de dados. Recebe os dados do produto, chama o serviço de criação e retorna a resposta. '''
    
    return create_product_service(db, product)

# Endpoint para deletar um produto do banco de dados. Recebe o ID do produto, chama o serviço de exclusão e retorna a resposta.
@router.delete("/{product_id}", status_code=204)
def delete_product(
        product_id: int, 
        db: Session = Depends(get_db), 
        current_user: User = Depends(get_current_user)
):
    
    ''' Endpoint para deletar um produto do banco de dados. Recebe o ID do produto, chama o serviço de exclusão e retorna a resposta. '''
    
    return delete_product_service(db, product_id)