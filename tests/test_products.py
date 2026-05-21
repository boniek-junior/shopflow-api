# Testa a listagem de produtos — rota pública
def test_get_products(client):
    response = client.get("/products/")

    assert response.status_code == 200
    assert "items" in response.json()
    assert "total" in response.json()
    assert isinstance(response.json()["items"], list)


# Testa a criação de um produto com usuário autenticado
def test_create_product(auth_client):
    response = auth_client.post("/products/", json={
        "name": "Camiseta",
        "description": "Camiseta preta",
        "price": 59.90,
        "stock": 100
    })

    assert response.status_code == 200
    assert response.json()["name"] == "Camiseta"
    assert response.json()["price"] == 59.90
    assert response.json()["is_active"] == True


# Testa que não é possível criar produto sem autenticação
def test_create_product_unauthorized(client):
    response = client.post("/products/", json={
        "name": "Camiseta",
        "description": "Camiseta preta",
        "price": 59.90,
        "stock": 100
    })

    assert response.status_code == 401


# Testa a busca de um produto por ID
def test_get_product_by_id(auth_client):
    # Cria o produto primeiro
    created = auth_client.post("/products/", json={
        "name": "Camiseta",
        "description": "Camiseta preta",
        "price": 59.90,
        "stock": 100
    })

    product_id = created.json()["id"]

    # Busca pelo ID
    response = auth_client.get(f"/products/{product_id}")

    assert response.status_code == 200
    assert response.json()["id"] == product_id


# Testa a busca de um produto que não existe
def test_get_product_not_found(client):
    response = client.get("/products/9999")

    assert response.status_code == 404


# Testa o soft delete de um produto
def test_delete_product(auth_client):
    # Cria o produto
    created = auth_client.post("/products/", json={
        "name": "Camiseta",
        "description": "Camiseta preta",
        "price": 59.90,
        "stock": 100
    })

    product_id = created.json()["id"]

    # Deleta o produto
    response = auth_client.delete(f"/products/{product_id}")
    assert response.status_code == 204

    # Confirma que o produto não aparece mais
    response = auth_client.get(f"/products/{product_id}")
    assert response.status_code == 404