from fastapi import HTTPException, status


# Exceção para recursos não encontrados (404)
class NotFoundException(HTTPException):
    def __init__(self, detail: str = "Recurso não encontrado"):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=detail
        )


# Exceção para acesso não autorizado (401)
class UnauthorizedException(HTTPException):
    def __init__(self, detail: str = "Não autorizado"):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            headers={"WWW-Authenticate": "Bearer"}
        )


# Exceção para acesso proibido (403)
class ForbiddenException(HTTPException):
    def __init__(self, detail: str = "Acesso negado"):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=detail
        )


# Exceção para conflitos (400) — ex: email já cadastrado
class BadRequestException(HTTPException):
    def __init__(self, detail: str = "Requisição inválida"):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail
        )