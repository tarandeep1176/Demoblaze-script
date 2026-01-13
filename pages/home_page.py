from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class HomePage:

    cat_phone = (By.CSS_SELECTOR, "a[onClick=\"byCat('phone')\"]")
    phone = (By.XPATH, "//a[text()='Nexus 6']")
    add_to_cart = (By.CSS_SELECTOR,".btn.btn-success.btn-lg")
    cart_btn = (By.CSS_SELECTOR,"#cartur")
    
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def add_to_cart(self):

        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable(*self.cat_phone)).click()
        self.wait.until(EC.element_to_be_clickable(*self.phone)).click()
        self.wait.until(EC.element_to_be_clickable(*self.add_to_cart)).click()
        self.wait.until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()
        time.sleep(2)

    def open_cart_page(self):
        self.wait.until(EC.element_to_be_clickable(*self.cart_btn)).click()
