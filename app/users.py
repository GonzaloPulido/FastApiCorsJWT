from http.client import HTTPException
from app.auth import create_access_token

fake_users_db = {"user1": {"username": "user1", "password": "password1", "name": "Gonzalo", "age": 23},
                 "user2": {"username": "user2", "password": "password2", "name": "Angel", "age": 23},
                 "user3": {"username": "user3", "password": "password3", "name": "Alvaro", "age": 23},
                 "user4": {"username": "user4", "password": "password4", "name": "Yeray", "age": 23},
                 "user5": {"username": "user5", "password": "password5", "name": "Rafa", "age": 23},
                }

def login(username: str, password: str):
    user = fake_users_db.get(username)
    
    if not user or user["password"] != password:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    
    access_token = create_access_token(data={"sub": username})
    return {"access_token": access_token, "token_type": "bearer"}

def logout():
    return {"message": "Logout exitoso, el token ha sido eliminado en el cliente."}
