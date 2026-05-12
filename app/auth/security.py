from passlib.context import CryptContext

# Senha de hash para proteger as senhas dos usuários
pwd_context = CryptContext(
    schemes=["bcrypt"], 
    deprecated="auto"
)

# Função para hash de senha, usando bcrypt para garantir a segurança das senhas dos usuários.
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Função para verificar a senha, comparando a senha fornecida com a senha hash armazenada no banco de dados.
def verify_password(
        password: str, 
        hashed_password: str
) -> bool:
    
    return pwd_context.verify(
        password, 
        hashed_password
    )