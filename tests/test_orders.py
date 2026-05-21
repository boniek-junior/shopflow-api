import pytest


# Fixture auxiliar que cria um produto e adiciona ao carrinho
@pytest.fixture()
def cart_with_item(auth_client):
    # Cria um produto
    product = auth_client.post("/products/", json={
        "name": "Camiseta",
        "description": "Camiseta preta",
        "price": 59.90,
        "stock": 100
    })

    product_id = product.json()["id"]

    # Adiciona ao carrinho
    auth_client.post("/cart/items", json={
        "product_id": product_id,
        "quantity": 2
    })

    return auth_client


# Testa o checkout com carrinho válido
def test_checkout_success(cart_with_item):
    response = cart_with_item.post("/orders/checkout")

    assert response.status_code == 200
    assert response.json()["status"] == "pendente"
    assert response.json()["total"] == 119.8
    assert len(response.json()["items"]) == 1


# Testa que o estoque é descontado após o checkout
def test_checkout_decreases_stock(cart_with_item):
    # Pega o produto antes do checkout
    products = cart_with_item.get("/products/")
    product_id = products.json()["items"][0]["id"]
    stock_before = products.json()["items"][0]["stock"]

    # Faz o checkout
    cart_with_item.post("/orders/checkout")

    # Verifica o estoque depois
    product_after = cart_with_item.get(f"/products/{product_id}")
    stock_after = product_after.json()["stock"]

    assert stock_after == stock_before - 2


# Testa que o carrinho é esvaziado após o checkout
def test_checkout_clears_cart(cart_with_item):
    cart_with_item.post("/orders/checkout")

    response = cart_with_item.get("/cart/")
    assert response.json()["items"] == []


# Testa checkout com carrinho vazio
def test_checkout_empty_cart(auth_client):
    response = auth_client.post("/orders/checkout")

    assert response.status_code == 400
    assert response.json()["detail"] == "Carrinho vazio"


# Testa a listagem do histórico de pedidos
def test_get_orders(cart_with_item):
    cart_with_item.post("/orders/checkout")

    response = cart_with_item.get("/orders/")

    assert response.status_code == 200
    assert len(response.json()) == 1


# Testa a busca de um pedido por ID
def test_get_order_by_id(cart_with_item):
    checkout = cart_with_item.post("/orders/checkout")
    order_id = checkout.json()["id"]

    response = cart_with_item.get(f"/orders/{order_id}")

    assert response.status_code == 200
    assert response.json()["id"] == order_id