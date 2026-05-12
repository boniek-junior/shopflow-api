# ShopFlow API

# API de e-commerce desenvolvida com Python, FastAPI e PostgreSQL, utilizando arquitetura Monólita Modular.

# O projeto foi criado com foco em escalabilidade, organização e aprendizado de práticas modernas de desenvolvimento backend.

# Tecnologias
Python
FastAPI
PostgreSQL
SQLAlchemy
Alembic
Docker
Pydantic
JWT Authentication
Funcionalidades Planejadas
Autenticação JWT
Cadastro de usuários
Login
CRUD de produtos
Carrinho de compras
Pedidos
Checkout
Simulação de pagamentos

# Estrutura do Projeto
shopflow-api/
│
├── app/
│   ├── core/
│   ├── users/
│   ├── shared/
│   └── main.py
│
├── alembic/
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md


# Como Executar o Projeto

# 1. Clonar o repositório
git clone https://github.com/boniek-junior/shopflow-api.git

# 2. Entrar na pasta
cd shopflow-api

# 3. Criar ambiente virtual
python -m venv .venv

# 4. Ativar ambiente virtual
Windows (Git Bash)
source .venv/Scripts/activate
Windows (PowerShell)
.venv\Scripts\Activate.ps1

# 5. Instalar dependências
pip install -r requirements.txt

# 6. Subir PostgreSQL com Docker
docker compose up -d

# 7. Executar migrations
alembic upgrade head

# 8. Rodar aplicação
uvicorn app.main:app --reload
Documentação da API

Após iniciar o servidor:

# Swagger UI:

http://127.0.0.1:8000/docs

# Redoc:

http://127.0.0.1:8000/redoc
Status do Projeto

🚧 Em desenvolvimento

# Autor

# Boniek Junior
