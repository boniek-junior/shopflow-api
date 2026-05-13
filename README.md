# ShopFlow API

## Descrição do Projeto

A **ShopFlow API** é uma API moderna de e-commerce construída com FastAPI, projetada para fornecer uma plataforma robusta e escalável para operações de comércio eletrônico. O projeto visa oferecer uma experiência completa de compra online, desde o registro de usuários até o processamento de pedidos e pagamentos.

### Funcionalidades Principais
- **Autenticação e Autorização**: Sistema de registro e login de usuários com JWT
- **Gerenciamento de Usuários**: CRUD completo para usuários
- **Catálogo de Produtos**: Gerenciamento de produtos, categorias e inventário
- **Carrinho de Compras**: Funcionalidades de adição, remoção e atualização de itens no carrinho
- **Pedidos**: Processamento e rastreamento de pedidos
- **Pagamentos**: Integração com sistemas de pagamento
- **Administração**: Painel administrativo para gerenciamento da loja

## Stack Tecnológica

- **Backend**: FastAPI (Python)
- **Banco de Dados**: PostgreSQL
- **ORM**: SQLAlchemy
- **Migrações**: Alembic
- **Autenticação**: JWT (python-jose)
- **Hash de Senhas**: bcrypt (passlib)
- **Configurações**: Pydantic Settings
- **Servidor ASGI**: Uvicorn
- **Containerização**: Docker & Docker Compose

## Pré-requisitos

- Python 3.8+
- Docker & Docker Compose
- Git

## Instalação e Configuração

### 1. Clone o repositório
```bash
git clone https://github.com/boniek-junior/shopflow-api.git
cd shopflow-api
```

### 2. Configure o ambiente virtual
```bash
python -m venv .venv
# No Windows:
.venv\Scripts\activate
# No Linux/Mac:
source .venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/shopflow
SECRET_KEY=sua-chave-secreta-aqui
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5. Execute o banco de dados
```bash
docker-compose up -d
```

### 6. Execute as migrações do banco
```bash
alembic upgrade head
```

### 7. Execute a aplicação
```bash
uvicorn app.main:app --reload
```

A API estará disponível em: http://localhost:8000

### Documentação da API
Acesse http://localhost:8000/docs para visualizar a documentação interativa gerada pelo Swagger.

## Estrutura do Projeto

```
shopflow-api/
├── alembic/                 # Migrações do banco de dados
├── app/
│   ├── auth/               # Módulo de autenticação
│   ├── cart/               # Módulo do carrinho de compras
│   ├── categories/         # Módulo de categorias
│   ├── core/               # Configurações centrais
│   ├── inventory/          # Módulo de inventário
│   ├── orders/             # Módulo de pedidos
│   ├── payments/           # Módulo de pagamentos
│   ├── products/           # Módulo de produtos
│   ├── shared/             # Utilitários compartilhados
│   └── users/              # Módulo de usuários
├── tests/                  # Testes da aplicação
├── Dockerfile              # Configuração Docker
├── docker-compose.yml      # Orquestração de containers
├── requirements.txt        # Dependências Python
└── README.md               # Este arquivo
```

## Funcionalidades Implementadas

### ✅ Autenticação
- Registro de usuários
- Login com JWT
- Validação de tokens

### ✅ Usuários
- Modelo de usuário com SQLAlchemy
- Repositório para operações no banco
- Serviço de negócio
- Schemas Pydantic
- Rotas CRUD

### 🚧 Em Desenvolvimento
- Catálogo de produtos
- Carrinho de compras
- Sistema de pedidos
- Integrações de pagamento
- Painel administrativo

## Funcionalidades Planejadas

### Fase 1: Core E-commerce (Em andamento)
- [x] Sistema de usuários e autenticação
- [ ] Gerenciamento de produtos e categorias
- [ ] Carrinho de compras básico

### Fase 2: Processamento de Pedidos
- [ ] Sistema de pedidos e checkout
- [ ] Integração com gateways de pagamento
- [ ] Controle de inventário

### Fase 3: Recursos Avançados
- [ ] Sistema de avaliações e comentários
- [ ] Recomendações personalizadas
- [ ] Notificações por email/SMS
- [ ] Relatórios administrativos
- [ ] API de integração com marketplaces

### Fase 4: Escalabilidade e Produção
- [ ] Cache com Redis
- [ ] Deploy em nuvem (Azure/AWS)
- [ ] CI/CD pipeline
- [ ] Monitoramento e logs
- [ ] Testes automatizados completos

## Como Contribuir

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

- Autor: Boniek Junior
- Email: boniek.junior.123@gmail.com
- GitHub: [boniek-junior](https://github.com/boniek-junior)
