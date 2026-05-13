from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.orm import sessionmaker, Session

from app.core.config import settings

# Configuração do banco de dados usando SQLAlchemy.
engine = create_engine(settings.DATABASE_URL)

# Criação de uma fábrica de sessões para interagir com o banco de dados.
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)

# Base para as classes de modelo do SQLAlchemy.
Base = declarative_base()

# Função para obter uma sessão de banco de dados.
def get_db():
    ''' Função para obter uma sessão de banco de dados. '''
    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()