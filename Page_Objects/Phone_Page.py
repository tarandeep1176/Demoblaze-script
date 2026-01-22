from selenium.webdriver.common.by import By

class PhonePageObjects:
    cat_phone = (By.CSS_SELECTOR, "a[onClick=\"byCat('phone')\"]")
    phone = (By.XPATH, "//a[text()='Nexus 6']")
    add_to_cart_btn = (By.CSS_SELECTOR,".btn.btn-success.btn-lg")
    cart_btn = (By.CSS_SELECTOR,"#cartur")