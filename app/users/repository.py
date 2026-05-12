from sqlalchemy.orm import Session

from app.users.models import User

# Repository de usuários, responsável por interagir com o banco de dados para operações relacionadas a usuários.

# Função para recuperar um usuário do banco de dados com base no email.
def get_user_by_email(
        db: Session, 
        email: str
) -> User:
   
    ''' Recupera um usuário do banco de dados com base no email. '''
    
    return (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

# Função para criar um novo usuário no banco de dados.
def create_user(
        db: Session, 
        name: str, 
        email: str, 
        password: str
) -> User:
    
    ''' Cria um novo usuário no banco de dados. '''
    
    user = User(
    name = name, 
    email = email, 
    password = password
)
    
    db.add(user)
    db.commit()
    db.refresh(user)
    return user