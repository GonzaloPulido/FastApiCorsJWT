from http.client import HTTPException
from app.schemas import LoginRequest, TokenRequest, LogoutRequest
from fastapi import FastAPI, Depends  # type: ignore
from app.auth import get_current_user, create_access_token
from app.users import login, logout
from fastapi.middleware.cors import CORSMiddleware # type: ignore


# Iniciar proyecto: uvicorn app.main:app --reload

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos los orígenes (puedes restringir esto a ["http://localhost:3000"] más adelante)
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

@app.get("/")
def home():
    return {"message": "Bienvenido a la API"}



@app.post("/token")
def login_endpoint(credentials: LoginRequest):
    if not credentials.username or not credentials.password:
        raise HTTPException(status_code=400, detail="Username y password son obligatorios")
    
    return login(credentials.username, credentials.password)


@app.post("/logout")
def logout_endpoint(logout_data: LogoutRequest):
    return {"message": "Logout exitoso"}

@app.post("/me")
def get_me(token_data: TokenRequest):
    try:
        user = get_current_user(token_data.token)  
        return user  
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
