from fastapi import FastAPI

from app.users.routes import router as users_router
from app.auth.routes import router as auth_router
from app.products.routes import router as products_router

# Criação da aplicação FastAPI e inclusão dos routers de usuários e autenticação.
app = FastAPI(
    title="ShopFlow API",
    version="1.0.0"
)
# Inclusão dos routers para usuários.
app.include_router(users_router)

# Inclusão dos routers para autenticação.
app.include_router(auth_router)

# Inclusão dos routers para produtos.
app.include_router(products_router)

# Endpoint raiz para verificar se a API está funcionando.
@app.get("/")
def root():
    return {"message": "ShopFlow API running"}