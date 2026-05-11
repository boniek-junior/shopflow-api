from fastapi import FastAPI

app = FastAPI(
    title="ShopFlow API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "ShopFlow API running"}