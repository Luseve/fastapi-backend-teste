# FastAPI backend de exemplo
from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def root():
    return {'mensagem': 'API funcionando'}