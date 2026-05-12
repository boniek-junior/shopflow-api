from pydantic import BaseModel, EmailStr

# Schemas para autenticação e gerenciamento de tokens
class LoginRequest(BaseModel):
    email: EmailStr
    password: str

# Schemas para criação e resposta de usuários
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"