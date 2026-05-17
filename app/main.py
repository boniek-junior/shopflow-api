from fastapi import FastAPI

# Criação da aplicação FastAPI e inclusão dos routers de usuários e autenticação.
app = FastAPI(
    title="ShopFlow API",
    version="1.0.0"
)
# Inclusão dos routers para usuários.
from app.users.routes import router as users_router
app.include_router(users_router)

# Inclusão dos routers para autenticação.
from app.auth.routes import router as auth_router
app.include_router(auth_router)

# Inclusão dos routers para produtos.
from app.products.routes import router as products_router
app.include_router(products_router)

# Inclusão dos routers para o carrinho de compras.
from app.cart.routes import router as cart_router
app.include_router(cart_router)

# Inclusão dos routers para pedidos.
from app.orders.routes import router as orders_router
app.include_router(orders_router)

# Endpoint raiz para verificar se a API está funcionando.
@app.get("/")
def root():
    return {"message": "ShopFlow API running"}