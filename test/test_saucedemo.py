import pytest
import sys
import os
from selenium.webdriver.common.by import By
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils.helpers import login_saucedemo, get_driver

@pytest.fixture

#iniciar la función para que los servicios se actualicen solos
def driver():
    driver  = get_driver()
    yield driver #selecciona el driver correcto
    driver.quit()

def test_login(driver):
    login_saucedemo(driver)

    assert "/inventory.html" in driver.current_url #saber en que página estoy
    titulo =  driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
    assert titulo == 'Products'

def test_catalogo(driver):
    login_saucedemo(driver)
    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    assert len(products) > 0 #verifica que existan productos

def test_carrito(driver):
    login_saucedemo()
    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    total_products = len(products)
    products[0].find_elements(By.TAG_NAME, 'button').click()