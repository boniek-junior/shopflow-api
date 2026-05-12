from passlib.context import CryptContext
import bcrypt

# Senha de hash para proteger as senhas dos usuários
pwd_context = CryptContext(
    schemes=["bcrypt"], 
    deprecated="auto"
)

# Função para hash de senha, usando bcrypt para garantir a segurança das senhas dos usuários.
def hash_password(password: str) -> str:
    return bcrypt.hashpw(
        password.encode('utf-8'),
        bcrypt.gensalt()
    ).decode('utf-8')

# Função para verificar a senha, comparando a senha fornecida com a senha hash armazenada no banco de dados.
def verify_password(
        password: str, 
        hashed_password: str
) -> bool:
    
    return bcrypt.checkpw(
        password.encode('utf-8'),
        hashed_password.encode('utf-8')
    )