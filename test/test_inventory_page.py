from page.login_page import LoginPage
from page.inventory_page import InventoryPage

#Verificar inventario
def test_inventory( driver ):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    login.open()
    #información para loggearse
    login.login("standard_user", "secret_sauce")
    inventory.is_at_page()
    inventory.logout()
    assert "https://www.saucedemo.com/" in driver.current_url