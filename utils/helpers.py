from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

URL = 'https://www.saucedemo.com/'
username = "standard_user"
password = "secret_sauce"


def get_driver(): #función para que los servicios se actualicen solos
    #Comienza con la pestaña en pantalla completa
    # options = Options
    # options.add_argument('--start-maximized')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    time.sleep(7)

    return driver

def login_saucedemo(driver):
    driver.get(URL)
    #ingresar las credenciales
    driver.find_element(By.NAME,"user-name").send_keys(username)
    driver.find_element(By.NAME,"password").send_keys(password)
    driver.find_element(By.ID,'login-button').click()

    time.sleep(7)

    