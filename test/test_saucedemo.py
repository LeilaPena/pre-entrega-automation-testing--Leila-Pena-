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

def test_carrito(driver):
    login_saucedemo(driver)
    products = driver.find_element(By.CLASS_NAME, 'inventory_item')
    assert len(products) > 0 #verifica que tenga contenido