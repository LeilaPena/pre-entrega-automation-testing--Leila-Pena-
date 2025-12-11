from page.login_page import LoginPage
from page.inventory_page import InventoryPage
from page.cart_page import CartPage
from page.checkout_page import CheckoutPage
import time

#hacer el curso parcial de una compra
def test_checkout_process(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.open()
    #información para loggearse
    login.login("standard_user", "secret_sauce")
    time.sleep(4)
    
    #agregar producto e ir al carro
    inventory.add_product_to_cart(0)
    inventory.go_to_cart()
    time.sleep(4)

    #Ir al checkout
    cart.go_to_checkout()
    time.sleep(3)
    
    assert checkout.is_at_page()
    
    #Completar checkout
    checkout.fill_customer_info("John", "Doe", "12345")
    checkout.continue_to_overview()
    
    #verificar que llegue al paso 2
    assert "checkout-step-two" in driver.current_url

#hacer el curso parcial de una compra sin completar los datos del checkout
def test_checkout_validation(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.open()
    #información para loggearse
    login.login("standard_user", "secret_sauce")
    
    #agregar producto e ir al carro
    inventory.add_product_to_cart(0)
    inventory.go_to_cart()
    #Ir al checkout
    cart.go_to_checkout()
    
    checkout.continue_to_overview()
    
    error_message = checkout.get_error_message()
    assert "First Name is required" in error_message