from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt
from fastapi import HTTPException, status

from app.core.config import settings

# Função para criar um token de acesso JWT com os dados fornecidos.
def create_access_token(data: dict) -> str:
    ''' Cria um token de acesso JWT com os dados fornecidos. '''
    
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

# Função para verificar a validade de um token de acesso JWT e retornar seus dados.
def verify_access_token(token: str) -> dict:
    ''' Verifica a validade de um token de acesso JWT e retorna seus dados. '''
    
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )