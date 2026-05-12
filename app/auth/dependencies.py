from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.users.repository import get_user_by_email
from app.auth.jwt_handler import verify_access_token
from app.users.models import User

# Dependência para obter o usuário autenticado a partir do token JWT. Verifica o token e retorna o usuário correspondente.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Dependência para obter o usuário autenticado a partir do token JWT. Verifica o token e retorna o usuário correspondente.
def get_current_user(
        token: str = Depends(oauth2_scheme), 
        db: Session = Depends(get_db)
) -> User:
    
    ''' Dependência para obter o usuário autenticado a partir do token JWT. Verifica o token e retorna o usuário correspondente. '''
    
    payload = verify_access_token(token)
    email = payload.get("sub")

    if not email:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    user = get_user_by_email(db, email)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário não encontrado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return user