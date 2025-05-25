from fastapi import APIRouter, HTTPException
from app.models.user import UserIn, UserOut
from app.models.core.security import hash_password

router = APIRouter(prefix="/auth", tags=["auth"])

fake_users_db = []
user_id_counter = 1

@router.post("/register", response_model=UserOut, status_code=201)
def register(user: UserIn):
    global user_id_counter

    for existing_user in fake_users_db:
        if existing_user["email"] == user.email:
            raise HTTPException(status_code=400, detail="E-mail já cadastrado")

    new_user = {
        "id": user_id_counter,
        "email": user.email,
        "full_name": user.full_name,
        "hashed_password": hash_password(user.password),
    }
    fake_users_db.append(new_user)
    user_id_counter += 1

    return new_user