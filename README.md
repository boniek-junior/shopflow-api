# ShopFlow API

<p align="center">
  <strong>API moderna para e-commerce, construida com FastAPI, PostgreSQL, SQLAlchemy e Alembic.</strong>
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-0.136.1-009688?style=for-the-badge&logo=fastapi&logoColor=white">
  <img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-16-4169E1?style=for-the-badge&logo=postgresql&logoColor=white">
  <img alt="Alembic" src="https://img.shields.io/badge/Alembic-Migrations-222222?style=for-the-badge">
</p>

## Sobre o projeto

O **ShopFlow API** e o backend de uma aplicacao de e-commerce. Nesta versao inicial, o projeto ja possui uma base organizada para evolucao da API, com configuracao por variaveis de ambiente, conexao com PostgreSQL, migracoes de banco com Alembic e estrutura modular para dominios da aplicacao.

### Recursos atuais

- API FastAPI configurada com titulo e versao.
- Endpoint raiz para health check simples.
- PostgreSQL local via Docker Compose.
- SQLAlchemy como ORM.
- Alembic para versionamento do banco de dados.
- Modelo inicial de usuarios.
- Configuracao centralizada com `pydantic-settings`.

## Tecnologias

| Categoria | Ferramentas |
| --- | --- |
| API | FastAPI, Starlette, Uvicorn |
| Banco de dados | PostgreSQL 16, SQLAlchemy |
| Migracoes | Alembic |
| Configuracao | Pydantic Settings, python-dotenv |
| Seguranca | Passlib, bcrypt, python-jose |
| Ambiente | Docker Compose, virtualenv |

## Estrutura do projeto

```text
shopflow-api/
|-- alembic/
|   |-- versions/
|   |   `-- 0b4a6838d91b_create_users_table.py
|   |-- env.py
|   `-- script.py.mako
|-- app/
|   |-- core/
|   |   |-- config.py
|   |   |-- database.py
|   |   |-- security.py
|   |   `-- settings.py
|   |-- users/
|   |   `-- models.py
|   |-- main.py
|   `-- test_db.py
|-- tests/
|-- alembic.ini
|-- docker-compose.yml
|-- requirements.txt
`-- README.md
```

## Primeiros passos

### Pre-requisitos

Antes de iniciar, tenha instalado:

- Python 3.11 ou superior.
- Docker e Docker Compose.
- Git.

### 1. Clone o repositorio

```bash
git clone <url-do-repositorio>
cd shopflow-api
```

### 2. Crie e ative o ambiente virtual

No Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

No Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependencias

```bash
pip install -r requirements.txt
```

### 4. Configure as variaveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/shopflow
SECRET_KEY=sua-chave-secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

> Use uma chave segura em `SECRET_KEY` antes de publicar ou subir a aplicacao em producao.

### 5. Suba o banco de dados

```bash
docker compose up -d
```

O servico cria um banco PostgreSQL com as seguintes credenciais locais:

| Campo | Valor |
| --- | --- |
| Host | `localhost` |
| Porta | `5432` |
| Database | `shopflow` |
| Usuario | `postgres` |
| Senha | `postgres` |

### 6. Execute as migracoes

```bash
alembic upgrade head
```

### 7. Inicie a API

```bash
uvicorn app.main:app --reload
```

A aplicacao ficara disponivel em:

- API: `http://127.0.0.1:8000`
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Endpoints disponiveis

| Metodo | Rota | Descricao |
| --- | --- | --- |
| `GET` | `/` | Retorna uma mensagem confirmando que a API esta em execucao. |

Resposta esperada:

```json
{
  "message": "ShopFlow API running"
}
```

## Banco de dados

### Modelo `User`

A tabela `users` e criada pela migracao inicial e possui os seguintes campos:

| Campo | Tipo | Regras |
| --- | --- | --- |
| `id` | Integer | Chave primaria, indexado |
| `name` | String | Indexado |
| `email` | String | Unico, indexado |
| `password` | String | Senha do usuario |

### Comandos uteis do Alembic

Criar uma nova migracao automaticamente:

```bash
alembic revision --autogenerate -m "descricao da migracao"
```

Aplicar migracoes pendentes:

```bash
alembic upgrade head
```

Reverter a ultima migracao:

```bash
alembic downgrade -1
```

Ver historico de migracoes:

```bash
alembic history
```

## Verificando a conexao com o banco

O projeto possui um script simples para testar a conexao configurada em `DATABASE_URL`:

```bash
python -m app.test_db
```

Se tudo estiver correto, o script exibira uma mensagem de sucesso no terminal.

## Scripts uteis

| Acao | Comando |
| --- | --- |
| Subir banco | `docker compose up -d` |
| Parar banco | `docker compose down` |
| Instalar dependencias | `pip install -r requirements.txt` |
| Rodar API | `uvicorn app.main:app --reload` |
| Aplicar migracoes | `alembic upgrade head` |
| Testar conexao | `python -m app.test_db` |

## Boas praticas para evolucao

- Criar routers por dominio dentro de `app/`.
- Manter modelos SQLAlchemy proximos ao dominio correspondente.
- Adicionar schemas Pydantic para entrada e saida de dados.
- Nunca versionar arquivos `.env` com credenciais reais.
- Criar testes automatizados dentro da pasta `tests/`.
- Gerar uma nova migracao sempre que o schema do banco mudar.

## Roadmap sugerido

- Cadastro e autenticacao de usuarios.
- Login com JWT.
- CRUD de produtos.
- Carrinho de compras.
- Pedidos e pagamentos.
- Testes automatizados.
- Dockerfile para empacotar a API.
- Pipeline de CI.

## Licenca

Este projeto esta sob a licenca MIT. Consulte o arquivo [`LICENSE`](LICENSE) para mais detalhes.
