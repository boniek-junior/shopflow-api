from sqlalchemy.orm import Session

from app.cart.models import Cart, CartItem

# Funções de repositório para manipular o carrinho de compras e seus itens no banco de dados.

# Função para obter o carrinho de compras de um usuário pelo ID do usuário.
def get_cart_by_user_id(db: Session, user_id: int) -> Cart | None:
    ''' Recupera o carrinho de compras de um usuário pelo ID do usuário. '''
    
    return db.query(Cart).filter(Cart.user_id == user_id).first()

# Função para criar um novo carrinho de compras para um usuário.
def create_cart(db: Session, user_id: int) -> Cart:
    ''' Cria um novo carrinho de compras para um usuário. '''
    
    cart = Cart(user_id=user_id)
    db.add(cart)
    db.commit()
    db.refresh(cart)
    return cart

# Função para obter um item do carrinho pelo ID do carrinho e ID do produto.
def get_cart_item(db: Session, cart_id: int, product_id: int) -> CartItem | None:
    ''' Recupera um item do carrinho pelo ID do carrinho e ID do produto. '''
    
    return db.query(CartItem).filter(
        CartItem.cart_id == cart_id,
        CartItem.product_id == product_id
    ).first()

# Função para adicionar um item ao carrinho de compras.
def add_item_to_cart(db: Session, cart_id: int, product_id: int, quantity: int) -> CartItem:
    ''' Adiciona um item ao carrinho de compras. '''
    
    item = CartItem(cart_id=cart_id, product_id=product_id, quantity=quantity)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

# Função para atualizar a quantidade de um item no carrinho de compras.
def update_cart_item_quantity(db: Session, item: CartItem, quantity: int) -> CartItem:
    ''' Atualiza a quantidade de um item no carrinho de compras. '''
    
    item.quantity = quantity
    db.commit()
    db.refresh(item)
    return item

# Função para remover um item do carrinho de compras.
def remove_item_from_cart(db: Session, item: CartItem) -> None:
    ''' Remove um item do carrinho de compras. '''
    
    db.delete(item)
    db.commit()