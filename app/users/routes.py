from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.users.schemas import UserCreate, UserResponse

from app.users.service import create_user_service

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/", response_model=UserResponse)
def create_user(
        user: UserCreate, 
        db: Session = Depends(get_db)
) -> UserResponse:
    
    ''' Endpoint para criar um novo usuário. Recebe os dados do usuário, chama o serviço de criação e retorna a resposta. '''
    
    return create_user_service(db, user)