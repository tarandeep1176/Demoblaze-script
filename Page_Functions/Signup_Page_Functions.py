from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Objects.Signup_Page import SignupPageObjects
import time

class SignupPageFunctions(SignupPageObjects):

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_signup(self):
        self.wait.until(EC.element_to_be_clickable(self.signup_btn)).click()
        self.wait.until(EC.visibility_of_element_located(self.signup_username))
        time.sleep(2)  

    def enter_username(self,username):
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located(self.signup_username))
        self.driver.find_element(*self.signup_username).send_keys(username)

    def enter_password(self,password):
            time.sleep(1)
            self.driver.find_element(*self.signup_password).send_keys(password)

    def click_signup(self):
            self.driver.find_element(*self.submit_btn).click()
            time.sleep(1)
    
    def accept_signup_alert(self):
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        print("Alert Text:", alert.text)
        if(alert.text == "This user already exist."):
            alert.accept()
            self.driver.find_element(*self.close_btn).click()
        elif(alert.text == "Sign up successful."):
            alert.accept()

