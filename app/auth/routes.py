from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.auth.schemas import LoginRequest, TokenResponse
from app.auth.security import verify_password
from app.auth.jwt_handler import create_access_token
from app.users.repository import get_user_by_email

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/login", response_model=TokenResponse)
def login(credentials: LoginRequest, db: Session = Depends(get_db)) -> TokenResponse:
    
    ''' Endpoint para autenticação de usuários e geração de tokens JWT. '''
   
    user = get_user_by_email(db, credentials.email)
    if not user or not verify_password(credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha inválidos",
        )
    token = create_access_token(data={"sub": user.email})
    return TokenResponse(access_token=token)