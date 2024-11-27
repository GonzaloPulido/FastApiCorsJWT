from fastapi import HTTPException, Depends # type: ignore
from jose import JWTError, jwt # type: ignore
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer # type: ignore

fake_users_db = {"user1": {"username": "user1", "password": "password1", "name": "Gonzalo", "age": 23},
                 "user2": {"username": "user2", "password": "password2", "name": "Angel", "age": 23},
                 "user3": {"username": "user3", "password": "password3", "name": "Alvaro", "age": 23},
                 "user4": {"username": "user4", "password": "password4", "name": "Yeray", "age": 23},
                 "user5": {"username": "user5", "password": "password5", "name": "Rafa", "age": 23},
                }

SECRET_KEY = "supersecretkey123"  
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Verificar el token
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Usuario no autenticado")
        
        user = fake_users_db.get(username)
        if not user:
            raise HTTPException(status_code=401, detail="Usuario no encontrado")
        
        return user  
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")

