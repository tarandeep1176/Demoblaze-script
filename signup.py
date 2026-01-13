from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.maximize_window()


def valid_case():
    driver.get("https://www.demoblaze.com/")
    driver.find_element(By.CSS_SELECTOR,"#signin2").click()
    time.sleep(1)
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#sign-username")))
    
    driver.find_element(By.CSS_SELECTOR,"#sign-username").send_keys("anotheruser")
    driver.find_element(By.CSS_SELECTOR,"#sign-password").send_keys("anotheruser123@")
    driver.find_element(By.CSS_SELECTOR,"button[onclick='register()']").click()
    time.sleep(1)

    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("Alert Text:", alert.text)
    alert.accept()

time.sleep(2)
def already_exists_case():
    driver.get("https://www.demoblaze.com/")
    driver.find_element(By.CSS_SELECTOR,"#signin2").click()
    time.sleep(1)
    signup_title = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#sign-username")))
    print(signup_title)
    if(signup_title):
        driver.find_element(By.CSS_SELECTOR,"#sign-username").send_keys("newuser")
        driver.find_element(By.CSS_SELECTOR,"#sign-password").send_keys("new_user123@")
        driver.find_element(By.CSS_SELECTOR,"button[onclick='register()']").click()
        time.sleep(1)

        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        print("Alert Text:", alert.text)
        alert.accept()


valid_case()
already_exists_case()

driver.close()