from fastapi import FastAPI
from app.routers import auth

app = FastAPI(title="API Lu Estilo")
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "🚀 API da Lu Estilo está no ar!"}