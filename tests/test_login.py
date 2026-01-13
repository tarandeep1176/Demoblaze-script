from selenium import webdriver
from pages.login_page import LoginPage


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.demoblaze.com/")

login = LoginPage(driver)
login.open_login()
login.invalid_case()
login.user_not_exist_case()
login.valid_case()