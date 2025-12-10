from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

URL = 'https://www.saucedemo.com/'

def get_driver(): #función para que los servicios se actualicen solos
    options = Options()
    options.add_argument('--start-maximized') #Comienza con la pestaña en pantalla completa
    service = Service(ChromeDriverManager().install()) #instalar el driver
    driver = webdriver.Chrome(service=service, options=options) #instalar el driver
    driver.implicitly_wait(10)

    return driver

def get_file_path(file_name, folder="data"):
    current_file = os.path.dirname(__file__) #archivo actual
    file_path = os.path.join(current_file,"..",folder,file_name) #Ruta relativa

    return os.path.abspath(file_path) #Ruta absoluta