from pydantic import BaseModel # type: ignore

class LoginRequest(BaseModel):
    username: str
    password: str

class TokenRequest(BaseModel):
    token: str

class LogoutRequest(BaseModel):
    token: str