from selenium import webdriver
from pages.signup_page import SignupPage

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.demoblaze.com/")

signup = SignupPage(driver)
signup.open_signup()
# signup.user_signup("anotheruser","anotheruser123@")
signup.valid_case("Usseerrrr","user123@")
signup.already_exists_case("anotheruser","anotheruser123@")