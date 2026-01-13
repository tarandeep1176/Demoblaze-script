from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class LoginPage:
        login_btn = (By.CSS_SELECTOR,"#login2")
        login_username = (By.CSS_SELECTOR,"#loginusername")
        login_password = (By.CSS_SELECTOR,"#loginpassword")
        submit = (By.CSS_SELECTOR,"button[onclick='logIn()']")
        welcome_text = (By.CSS_SELECTOR,"#nameofuser")


        def __init__(self,driver):
                self.driver = driver
                self.wait = WebDriverWait(driver, 15)

        def open_login(self):
                time.sleep(3)  
                self.driver.find_element(*self.login_btn).click()  
                self.wait.until(EC.visibility_of_element_located(*self.login_username))
                time.sleep(2)  

        def invalid_case(self):
                time.sleep(2)
                self.wait.until(EC.visibility_of_element_located(*self.login_username))
                self.driver.find_element(*self.login_username).send_keys("tarandeep.1176@zenmonk.tech")
                self.driver.find_element(*self.login_password).send_keys("Taran123@")
                self.driver.find_element(*self.submit).click()
                time.sleep(2)
                self.wait.until(EC.alert_is_present())
                alert = self.driver.switch_to.alert
                print("Alert Text:", alert.text)
                alert.accept()

        
        def user_not_exist_case(self):
                self.driver.find_element(By.CSS_SELECTOR,"#logInModal .btn-secondary").click()
                self.open_login()
                time.sleep(2)
                self.driver.find_element(*self.login_username).clear()
                self.driver.find_element(*self.login_password).clear()
                self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#loginusername")))
                self.driver.find_element(*self.login_username).send_keys("tarandeeppp.1176@zenmonk.tech")
                self.driver.find_element(*self.login_password).send_keys("taran123@")
                self.driver.find_element(*self.submit).click()
                time.sleep(2)
                self.wait.until(EC.alert_is_present())
                alert = self.driver.switch_to.alert
                print("Alert Text:", alert.text)
                alert.accept()

        
        def valid_case(self):
                self.driver.find_element(By.CSS_SELECTOR,"#logInModal .btn-secondary").click()
                self.open_login()
                time.sleep(1)
                self.driver.find_element(*self.login_username).clear()
                self.driver.find_element(*self.login_password).clear()
                self.wait.until(EC.visibility_of_element_located((By.ID,"loginusername")))
                self.driver.find_element(*self.login_username).send_keys("tarandeep.1176@zenmonk.tech")
                self.driver.find_element(*self.login_password).send_keys("taran123@")
                self.driver.find_element(*self.submit).click()
                time.sleep(1)
                welcome_text = self.wait.until(EC.visibility_of_element_located(*self.welcome_text))
                if(welcome_text):
                        print("Login successful! - ",welcome_text.text)
