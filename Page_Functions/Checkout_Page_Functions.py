from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Data.Checkout_Page_Data import CheckoutPageMother
from Page_Objects.Checkout_Page import CheckoutPageObjects
import time
import random 
import os
class CheckoutPageFunctions(CheckoutPageObjects):
    
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def place_order(self,data:CheckoutPageMother):
        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable(self.place_order_btn)).click()
        self.wait.until(EC.visibility_of_element_located(self.place_order_form))
        time.sleep(2)
        self.driver.find_element(*self.name).send_keys(data.name)
        time.sleep(2)
        self.driver.find_element(*self.country).send_keys(data.country)
        time.sleep(2)
        self.driver.find_element(*self.city).send_keys(data.city)
        time.sleep(2)
        self.driver.find_element(*self.credit_card).send_keys(data.credit_card_number)  
        time.sleep(2)
        self.driver.find_element(*self.month).send_keys(data.month)
        time.sleep(2)
        self.driver.find_element(*self.year).send_keys(data.year)
        time.sleep(2)
        self.driver.find_element(*self.purchase_order_btn).click()
        time.sleep(3)
        success_msg = self.wait.until(EC.visibility_of_element_located(self.order_success_msg))
        print("Order placed successfully:", success_msg.text)

    def get_order_details(self):
        details = self.wait.until(EC.visibility_of_element_located(self.order__details))
        print("Details of your order :- ", details.text)
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(self.details_box_ok)).click()
        time.sleep(3)
