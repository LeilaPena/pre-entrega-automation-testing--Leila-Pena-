from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    first_name_input = (By.ID, 'first-name')
    last_name_input = (By.ID, 'last-name')
    postal_code_input = (By.ID, 'postal-code')
    continue_button = (By.ID, "continue")
    cancel_button = (By.ID, 'cancel')
    error_message = (By.CLASS_NAME, 'error-message-container')

    def __init__(self, driver):
        self.driver = driver

    def is_at_page(self):
        return '/checkout-step-one.html' in self.driver.current_url

    def fill_customer_info(self, first_name, last_name, postal_code):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.first_name_input)
        ).send_keys(first_name)
        
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)

    def continue_to_overview(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.continue_button)
        ).click()
        
    def cancel_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cancel_button)
        ).click()

    def get_error_message(self):
        try:
            error_element = self.driver.find_element(*self.error_message)
            return error_element.text
        except:
            return ""