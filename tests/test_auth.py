# Testa o login com credenciais válidas
def test_login_success(client):
    # Cria o usuário primeiro
    client.post("/users/", json={
        "name": "Teste",
        "email": "teste@email.com",
        "password": "123456"
    })

    # Tenta fazer login
    response = client.post("/auth/login", json={
        "email": "teste@email.com",
        "password": "123456"
    })

    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"


# Testa o login com senha errada
def test_login_wrong_password(client):
    client.post("/users/", json={
        "name": "Teste",
        "email": "teste@email.com",
        "password": "123456"
    })

    response = client.post("/auth/login", json={
        "email": "teste@email.com",
        "password": "senhaerrada"
    })

    assert response.status_code == 401
    assert response.json()["detail"] == "Email ou senha inválidos"


# Testa o login com email que não existe
def test_login_user_not_found(client):
    response = client.post("/auth/login", json={
        "email": "naoexiste@email.com",
        "password": "123456"
    })

    assert response.status_code == 401
    assert response.json()["detail"] == "Email ou senha inválidos"