import pytest
from page.login_page import LoginPage
from page.inventory_page import InventoryPage
from page.cart_page import CartPage
import time


def test_cart_operations(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")
    
    inventory.add_product_to_cart(0)
    inventory.go_to_cart()
    
    assert cart.is_at_page()
    assert cart.get_cart_items_count() == 1
    
    cart.continue_shopping()
    assert inventory.is_at_page()

def test_remove_from_cart(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")
    
    inventory.add_product_to_cart(0)
    inventory.go_to_cart()
    
    initial_count = cart.get_cart_items_count()
    cart.remove_item(0)
    
    assert cart.get_cart_items_count() == initial_count - 1