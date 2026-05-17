import pytest


# Testa o cadastro de um novo usuário com dados válidos
def test_create_user(client):
    response = client.post("/users/", json={
        "name": "Cliente",
        "email": "cliente@email.com",
        "password": "123456"
    })

    assert response.status_code == 200
    assert response.json()["name"] == "Cliente"
    assert response.json()["email"] == "cliente@email.com"
    # garante que a senha nunca é retornada na resposta
    assert "password" not in response.json()


# Testa que não é possível cadastrar dois usuários com o mesmo email
def test_create_user_duplicate_email(client):
    # Cria o primeiro usuário
    client.post("/users/", json={
        "name": "Cliente",
        "email": "cliente@email.com",
        "password": "123456"
    })

    # Tenta criar outro com o mesmo email
    response = client.post("/users/", json={
        "name": "Outro",
        "email": "cliente@email.com",
        "password": "654321"
    })

    assert response.status_code == 400
    assert response.json()["detail"] == "Email já registrado"


# Testa que a rota /me retorna os dados do usuário autenticado
def test_get_me(auth_client):
    response = auth_client.get("/users/me")

    assert response.status_code == 200
    assert response.json()["email"] == "teste@email.com"


# Testa que a rota /me retorna 401 sem token
def test_get_me_unauthorized(client):
    response = client.get("/users/me")

    assert response.status_code == 401