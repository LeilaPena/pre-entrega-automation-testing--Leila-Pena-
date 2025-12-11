from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import URL
from selenium.webdriver.common.by import By

class LoginPage:

    campo_username = (By.NAME, 'user-name')
    campo_password = (By.NAME, 'password')
    login_button = (By.NAME, 'login-button')
    
    def __init__(self,  driver):
        self.driver = driver
    def open (self):
        self.driver.get(URL)

    def login(self, username, password):

        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.campo_password)).send_keys(password) #valida si existe el campo password
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.campo_username)).send_keys(username) #valida si existe el campo username
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.login_button)).click() #valida si existe el login button

