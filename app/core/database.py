from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.orm import sessionmaker, Session

from app.core.config import settings

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/shopflow"

engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)

Base = declarative_base()

def get_db():
    ''' Função para obter uma sessão de banco de dados. '''
    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()