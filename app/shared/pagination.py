from pydantic import BaseModel
from typing import TypeVar, Generic, List

T = TypeVar('T')


# Schema genérico de paginação — funciona para qualquer tipo de dado
class PaginatedResponse(BaseModel, Generic[T]):
    items: List[T]        # lista de itens da página atual
    total: int            # total de registros no banco
    page: int             # página atual
    page_size: int        # quantidade de itens por página
    total_pages: int      # total de páginas


# Parâmetros de paginação recebidos na requisição
class PaginationParams(BaseModel):
    page: int = 1         # página atual (padrão: 1)
    page_size: int = 10   # itens por página (padrão: 10)

    # Calcula o offset para a query do banco
    @property
    def offset(self) -> int:
        return (self.page - 1) * self.page_size