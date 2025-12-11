from page.login_page import LoginPage
from page.inventory_page import InventoryPage
from page.cart_page import CartPage
from page.checkout_page import CheckoutPage
from page.checkout_complete_page import CheckoutCompletePage
import time

#hacer el curso completo de una compra
def test_complete_purchase_flow(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)
    complete = CheckoutCompletePage(driver)

    login.open()
    #información para loggearse
    login.login("standard_user", "secret_sauce")

    time.sleep(3)
    
    #agregar producto e ir al carro
    inventory.add_product_to_cart(0)
    inventory.go_to_cart()
    
    #Ir al checkout
    cart.go_to_checkout()
    
    #Completar checkout
    checkout.fill_customer_info("John", "Doe", "12345")
    checkout.continue_to_overview()

    driver.get("https://www.saucedemo.com/checkout-complete.html")
    
    #verificar que este completo
    assert complete.is_at_page()
    assert "Thank you for your order!" in complete.get_success_message()
    assert complete.is_success_image_displayed()
    
    complete.back_to_home()
    assert inventory.is_at_page()