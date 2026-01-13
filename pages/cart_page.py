from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CartPage:

    place_order_btn = (By.CSS_SELECTOR,".btn.btn-success")
    place_order_form = (By.CSS_SELECTOR,"#orderModalLabel")
    name = (By.CSS_SELECTOR,"#name")
    country = (By.CSS_SELECTOR,"#country")
    city = (By.CSS_SELECTOR,"#city")
    credit_card = (By.CSS_SELECTOR,"#card")
    month = (By.CSS_SELECTOR,"#month")
    year = (By.CSS_SELECTOR,"#year")
    purchase_order_btn = (By.CSS_SELECTOR,"button[onclick='purchaseOrder()']")
    order_success_msg = (By.XPATH, "//h2[text()='Thank you for your purchase!']")
    order__details = (By.CSS_SELECTOR, ".lead.text-muted")
    details_box_ok = (By.CSS_SELECTOR,".confirm.btn.btn-lg.btn-primary")
    
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def place_order(self):
        self.wait.until(EC.element_to_be_clickable(*self.place_order_btn)).click()
        self.wait.until(EC.visibility_of_element_located(*self.place_order_form))
        time.sleep(2)
        self.driver.find_element(*self.name).send_keys("new_userrrrr")
        self.driver.find_element(*self.country).send_keys("India")
        self.driver.find_element(*self.city).send_keys("Delhi")
        self.driver.find_element(*self.credit_card).send_keys("6373478837434")  
        self.driver.find_element(*self.month).send_keys("January")
        self.driver.find_element(*self.year).send_keys("2026")
        self.driver.find_element(*self.purchase_order_btn).click()
        time.sleep(3)
        success_msg = self.wait.until(EC.visibility_of_element_located(*self.order_success_msg))
        print("Order placed successfully:", success_msg.text)

    def get_order_details(self):
        details = self.wait.until(EC.visibility_of_element_located(*self.order__details))
        print("Details of your order :- ", details.text)

        self.wait.until(EC.element_to_be_clickable(*self.details_box_ok)).click()
