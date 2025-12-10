from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    current_URL = '/cart.html'
    checkout_button = (By.ID, 'checkout')
    continue_shopping_button =(By.ID, 'continue-shopping')
    cart_item = (By.CLASS_NAME, 'cart_item')
    remove_button = (By.XPATH, "//button[contains(text(), 'Remove')]")
    cart_badge = (By.CLASS_NAME, 'shopping_cart_badge')
    

    def __init__(self, driver):
        self.driver = driver
        driver.implicitly_wait(5)

    def is_at_page(self):
         return self.current_URL in self.driver.current_url
    
    def go_to_checkout(self):
         WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.checkout_button)).click()

    def continue_shopping(self):
         WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.continue_shopping_button)).click()
    
    def get_cart_items_count(self):
         items =  self.driver.find_elements(*self.cart_item)
         return len(items)
    
    def remove_item(self, item_index=0):
        remove_buttons = self.driver.find_elements(*self.remove_button)
        if remove_buttons and item_index < len(remove_buttons):
             remove_buttons[item_index].click()

    def get_cart_badge_count(self):
        try:
            badge = self.driver.find_element(*self.cart_badge)
        except:
             return 0