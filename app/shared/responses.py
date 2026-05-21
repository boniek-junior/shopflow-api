from pydantic import BaseModel
from typing import TypeVar, Generic, Optional

T = TypeVar('T')


# Resposta padrão de sucesso com dados
class SuccessResponse(BaseModel, Generic[T]):
    success: bool = True
    message: str
    data: Optional[T] = None


# Resposta padrão de erro
class ErrorResponse(BaseModel):
    success: bool = False
    message: str
    detail: Optional[str] = None


# Resposta simples de sucesso sem dados — ex: delete, logout
class MessageResponse(BaseModel):
    success: bool = True
    message: str