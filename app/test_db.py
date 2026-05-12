from app.core.database import engine

try:
    connection = engine.connect()
    print("Conexão com banco OK!")
    connection.close()

except Exception as e:
    print("Erro:", e)