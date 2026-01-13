from selenium import webdriver
from pages.home_page import HomePage


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.demoblaze.com/")

home = HomePage(driver)
home.add_to_cart()
home.open_cart_page()