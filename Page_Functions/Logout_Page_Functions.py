from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Objects.Logout import LogoutPageObjects
import time

class LogoutPageFunctions(LogoutPageObjects):
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        
    def logout_user(self):
        self.wait.until(EC.element_to_be_clickable(self.logout_btn)).click()
        print("User logged out!")
