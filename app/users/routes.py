from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.users.schemas import UserCreate, UserResponse
from app.users.service import create_user_service
from app.auth.dependencies import get_current_user
from app.users.models import User


# Roteador para endpoints de usuários, incluindo criação de novos usuários.
router = APIRouter(
    prefix="/users",
    tags=["users"]
)

# Endpoint para criar um novo usuário. Recebe os dados do usuário, chama o serviço de criação e retorna a resposta.
@router.post("/", response_model=UserResponse)
def create_user(
        user: UserCreate, 
        db: Session = Depends(get_db)
) -> UserResponse:
    
    ''' Endpoint para criar um novo usuário. Recebe os dados do usuário, chama o serviço de criação e retorna a resposta. '''
    
    return create_user_service(db, user)

@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)) -> UserResponse:
    
    ''' Endpoint para obter os dados do usuário autenticado. Retorna as informações do usuário atual. '''
    
    return current_user