from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Objects.Phone_Page import PhonePageObjects
import time

class PhonePageFunctions(PhonePageObjects):
    
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def add_to_cart(self):

        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable(self.cat_phone)).click()
        self.wait.until(EC.element_to_be_clickable(self.phone)).click()
        self.wait.until(EC.element_to_be_clickable(self.add_to_cart_btn)).click()
        self.wait.until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()
        time.sleep(2)

    def open_cart_page(self):
        self.wait.until(EC.element_to_be_clickable(self.cart_btn)).click()