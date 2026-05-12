from pydantic import BaseModel, EmailStr


# Schemas para criação e resposta de usuários
class UserCreate(BaseModel):
    nome: str
    email: EmailStr
    password: str

# Schema para resposta de usuário, incluindo o ID gerado pelo banco de dados.
class UserResponse(BaseModel):
    id: int
    nome: str
    email: EmailStr

    class Config:
        from_attributes = True