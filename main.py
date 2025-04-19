
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import jwt

app = FastAPI()
SECRET_KEY = "steveanaliz_secret"

users_db = {}

class User(BaseModel):
    email: str
    password: str

@app.post("/register")
def register(user: User):
    if user.email in users_db:
        raise HTTPException(status_code=400, detail="Kullanıcı zaten kayıtlı")
    users_db[user.email] = user.password
    return {"message": "Kayıt başarılı"}

@app.post("/login")
def login(user: User):
    if users_db.get(user.email) != user.password:
        raise HTTPException(status_code=401, detail="Geçersiz giriş bilgileri")
    token = jwt.encode({"email": user.email}, SECRET_KEY, algorithm="HS256")
    return {"token": token}

@app.get("/users")
def get_users():
    return {"users": list(users_db.keys())}
