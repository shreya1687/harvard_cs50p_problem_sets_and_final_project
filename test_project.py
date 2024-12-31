import pytest
from project import ShoppingCart, Item


def test_calculate_total_bill():
    cart = ShoppingCart()
    cart.shopping_list = {3: ['aluminium_foil', 1, '1 l', 'pantry_essential'], 6: ['shampoo', 1, '1 l', 'toileteries_cosmetic']}
    assert cart.calculate_total_bill() == 400

def test_add_item_to_cart():
    cart = ShoppingCart()
    item = Item()
    item_info = item.item.item_list.get(str("5"))
    cart.shopping_list[5] = item_info
    assert 5 in cart.shopping_list
    assert cart.shopping_list[5] == ['toothpaste', 1, '1 l', 'toileteries_cosmetic']
    
def test_remove_item_from_cart():
    cart = ShoppingCart()
    cart.shopping_list = {}
    assert cart.shopping_list.keys() == "No items added in the shopping cart!"