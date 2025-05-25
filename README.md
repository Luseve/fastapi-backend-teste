# API Lu Estilo - Backend FastAPI

🚀 API desenvolvida como parte de um teste técnico para vaga de Desenvolvedor Backend.

## 🔧 Tecnologias Utilizadas
- Python 3.11+
- FastAPI
- Uvicorn
- PostgreSQL (via Docker)
- PyJWT
- HTTP Bearer Token (JWT)
- Pytest

## 🔐 Funcionalidades
- Registro de usuários com senha criptografada
- Login com JWT
- CRUD de clientes, produtos e pedidos
- Integração com WhatsApp (simulada)
- Rotas protegidas por níveis de acesso

## 📦 Instalação

```bash
# 1. Clonar repositório
git clone https://github.com/Luseve/fastapi-backend-teste.git
cd fastapi-backend-teste

# 2. Criar ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Rodar API
uvicorn app.main:app --reload
