from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.demoblaze.com/")
time.sleep(3)
wait = WebDriverWait(driver, 15)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[onClick=\"byCat('phone')\"]"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Nexus 6']"))).click()
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".btn.btn-success.btn-lg"))).click()
WebDriverWait(driver,10).until(EC.alert_is_present())
driver.switch_to.alert.accept()
time.sleep(2)
wait.until(EC.element_to_be_clickable(((By.CSS_SELECTOR,"#cartur")))).click()
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".btn.btn-success"))).click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#orderModalLabel")))
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"#name").send_keys("new_userrrrr")
driver.find_element(By.CSS_SELECTOR,"#country").send_keys("India")
driver.find_element(By.CSS_SELECTOR,"#city").send_keys("Delhi")
driver.find_element(By.CSS_SELECTOR,"#card").send_keys("6373478837434")  
driver.find_element(By.CSS_SELECTOR,"#month").send_keys("January")
driver.find_element(By.CSS_SELECTOR,"#year").send_keys("2026")
driver.find_element(By.CSS_SELECTOR,"button[onclick='purchaseOrder()']").click()
time.sleep(3)
success_msg = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Thank you for your purchase!']")))
print("Order placed successfully:", success_msg.text)


details = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".lead.text-muted")))
print("Details of your order :- ", details.text)

wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".confirm.btn.btn-lg.btn-primary"))).click()


driver.close()