import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.core.database import Base, get_db

# URL do banco de testes usando SQLite em memória para garantir isolamento dos testes.
DATABASE_URL_TEST = "sqlite:///./test.db"

# Cria o engine de banco de dados para os testes, configurado para usar SQLite em memória. O parâmetro "check_same_thread" é definido como False para permitir o acesso ao banco de dados a partir de múltiplas threads, o que é necessário para os testes.
engine_test = create_engine(DATABASE_URL_TEST, connect_args={"check_same_thread": False})

# Cria a fábrica de sessões para o banco de testes, configurada para não realizar commit automático e não realizar flush automático. O bind é definido como o engine de teste criado anteriormente.
TestintgSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)

# Fixture que cria e destrói o banco de testes a cada sessão
@pytest.fixture(scope="session", autouse=True)
def setup_database():
    """Fixture para configurar o banco de dados de teste antes de rodar os testes e limpar após os testes."""
    # Cria todas as tabelas no banco de teste com base nos modelos definidos.
    Base.metadata.create_all(bind=engine_test)
    yield
    # Após os testes, remove o arquivo do banco de teste para garantir um ambiente limpo.
    Base.metadata.drop_all(bind=engine_test)

# Fixture que sobrescreve o get_db da aplicação pelo banco de testes
@pytest.fixture()
def db():
    connection = engine_test.connect()
    transaction = connection.begin()
    session = TestintgSessionLocal(bind=connection)

    yield session

    # Reverte todas as mudanças após cada teste - mantém os testes isolados
    session.close()
    transaction.rollback()
    connection.close()

# Fixture para criar um cliente de teste do FastAPI, que é usado para enviar requisições HTTP para a aplicação durante os testes. A dependência get_db é sobrescrita para usar o banco de testes, garantindo que as operações de banco de dados durante os testes sejam realizadas no ambiente de teste.
@pytest.fixture()
def client(db):
    # Sobrescreve a dependência get_db para usar o banco de testes durante os testes.
    def override_get_db():
        yield db

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()

@pytest.fixture()
def auth_client(client):
    # Cadastra o usuário de teste
    client.post("/users/", json={
        "name": "Teste",
        "email": "teste@email.com",
        "password": "123456"
    })

    # Realiza login para obter o token de autenticação
    response = client.post("/auth/login", json={
        "email": "teste@email.com",
        "password": "123456"
    })

    token = response.json()["access_token"]

    # Retorna o cliente com o header de autenticação
    client.headers.update({"Authorization": f"Bearer {token}"})
    return client