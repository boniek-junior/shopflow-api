from fastapi import FastAPI

from app.users.routes import router as users_router

app = FastAPI(
    title="ShopFlow API",
    version="1.0.0"
)

app.include_router(users_router)

@app.get("/")
def root():
    return {"message": "ShopFlow API running"}