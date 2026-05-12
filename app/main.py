from fastapi import FastAPI

from app.users.routes import router as users_router
from app.auth.routes import router as auth_router

# Criação da aplicação FastAPI e inclusão dos routers de usuários e autenticação.
app = FastAPI(
    title="ShopFlow API",
    version="1.0.0"
)
# Inclusão dos routers para usuários e autenticação.
app.include_router(users_router)
app.include_router(auth_router)

# Endpoint raiz para verificar se a API está funcionando.
@app.get("/")
def root():
    return {"message": "ShopFlow API running"}