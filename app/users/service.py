from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.users.schemas import UserCreate
from app.users.repository import get_user_by_email, create_user

from app.auth.security import hash_password

# Serviço de usuários, responsável por implementar a lógica de negócios relacionada a usuários.

# Serviço para criar um novo usuário. Verifica se o email já existe e, se não, cria o usuário.
def create_user_service(
        db: Session, 
        user: UserCreate
) -> UserCreate:
    
    ''' Serviço para criar um novo usuário. Verifica se o email já existe e, se não, cria o usuário. '''
    
    existing_user = get_user_by_email(db, user.email)
   
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email já registrado"
        )
    
    hashed_password = hash_password(user.password)
    
    return create_user(
        db,
        name=user.name,
        email=user.email,
        password=hashed_password
    )