from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.cart.repository import (
    get_cart_by_user_id,
    create_cart,
    get_cart_item,
    add_item_to_cart,
    update_cart_item_quantity,
    remove_item_from_cart
)

from app.products.repository import get_product_by_id

# Serviço para gerenciar o carrinho de compras, incluindo operações para obter o carrinho, adicionar itens, atualizar quantidades e remover itens.

# Função para obter o carrinho de compras de um usuário ou criar um novo se não existir.
def get_or_create_cart(db: Session, user_id: int):
    ''' Obtém o carrinho de compras de um usuário ou cria um novo se não existir. '''
    
    cart = get_cart_by_user_id(db, user_id)
    if not cart:
        cart = create_cart(db, user_id)
    return cart

# Função para retornar o carrinho de compras de um usuário.
def get_cart_service(db: Session, user_id: int):
    ''' Serviço para obter o carrinho de compras de um usuário. '''
    
    cart = get_or_create_cart(db, user_id)
    return cart

# Função para adicionar um item ao carrinho de compras de um usuário.
def add_item_to_cart_service(db: Session, user_id: int, product_id: int, quantity: int):
    ''' Serviço para adicionar um item ao carrinho de compras de um usuário. '''
    
    product = get_product_by_id(db, product_id)
    cart = get_or_create_cart(db, user_id)
    
    if not product or not product.is_active:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    if quantity < 1:
        raise HTTPException(status_code=400, detail="Quantidade deve ser maior que zero")
    
    if product.stock < quantity:
        raise HTTPException(status_code=400, detail="Estoque insuficiente para o produto solicitado")
    
    existing_item = get_cart_item(db, cart.id, product_id)
    if existing_item:
        new_quantity = existing_item.quantity + quantity
        if product.stock < new_quantity:
            raise HTTPException(status_code=400, detail="Estoque insuficiente para a quantidade total solicitada")
        return update_cart_item_quantity(db, existing_item, new_quantity)
    
    return add_item_to_cart(db, cart.id, product_id, quantity)

# Função para remover um item do carrinho de compras de um usuário.
def remove_item_from_cart_service(db: Session, user_id: int, product_id: int):
    ''' Serviço para remover um item do carrinho de compras de um usuário. '''
    
    cart = get_or_create_cart(db, user_id)
    
    if not cart:
        raise HTTPException(status_code=404, detail="Carrinho de compras não encontrado")
    
    existing_item = get_cart_item(db, cart.id, product_id)

    if not existing_item:
        raise HTTPException(status_code=404, detail="Item do carrinho não encontrado")
    
    remove_item_from_cart(db, existing_item)