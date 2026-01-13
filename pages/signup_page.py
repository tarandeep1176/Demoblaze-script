from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SignupPage:

    signup_btn = (By.CSS_SELECTOR,"#signin2")
    signup_username = (By.CSS_SELECTOR,"#sign-username")
    signup_password = (By.CSS_SELECTOR,"#sign-password")
    submit_btn = (By.CSS_SELECTOR,"button[onclick='register()']")


    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_signup(self):
        time.sleep(3)  
        self.driver.find_element(*self.signup_btn).click()  
        self.wait.until(EC.visibility_of_element_located(*self.signup_username))
        time.sleep(2)  

    def valid_case(self,username,password):
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located(*self.signup_username))
        self.driver.find_element(*self.signup_username).send_keys(username)
        self.driver.find_element(*self.signup_password).send_keys(password)
        self.driver.find_element(*self.submit_btn).click()
        time.sleep(1)
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        print("Alert Text:", alert.text)
        alert.accept()


    def already_exists_case(self,username,password):
        self.driver.find_element(By.CSS_SELECTOR,"#signInModal .btn-secondary").click()
        self.open_signup()
        self.driver.find_element(*self.signup_username).clear()
        self.driver.find_element(*self.signup_password).clear()
        time.sleep(1)
        signup_title = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#sign-username")))
        print(signup_title)
        if(signup_title):
            self.driver.find_element(*self.signup_username).send_keys(username)
            self.driver.find_element(*self.signup_password).send_keys(password)
            self.driver.find_element(*self.submit_btn).click()
            time.sleep(1)
            self.wait.until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            print("Alert Text:", alert.text)
            alert.accept()

