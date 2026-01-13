from selenium import webdriver
from pages.cart_page import CartPage


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.demoblaze.com/cart.html")

cart = CartPage(driver)
cart.place_order()
cart.get_order_details()