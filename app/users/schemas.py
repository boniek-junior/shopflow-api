from pydantic import BaseModel, EmailStr


# Schemas para criação e resposta de usuários
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

# Schema para resposta de usuário, incluindo o ID gerado pelo banco de dados.
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True