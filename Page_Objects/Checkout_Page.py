from selenium.webdriver.common.by import By

class CheckoutPageObjects:
    place_order_btn = (By.CSS_SELECTOR,".btn.btn-success")
    place_order_form = (By.CSS_SELECTOR,"#orderModalLabel")
    name = (By.CSS_SELECTOR,"#name")
    country = (By.CSS_SELECTOR,"#country")
    city = (By.CSS_SELECTOR,"#city")
    credit_card = (By.CSS_SELECTOR,"#card")
    month = (By.CSS_SELECTOR,"#month")
    year = (By.CSS_SELECTOR,"#year")
    purchase_order_btn = (By.CSS_SELECTOR,"button[onclick='purchaseOrder()']")
    order_success_msg = (By.XPATH, "//h2[text()='Thank you for your purchase!']")
    order__details = (By.CSS_SELECTOR, ".lead.text-muted")
    details_box_ok = (By.CSS_SELECTOR,".confirm.btn.btn-lg.btn-primary")
    order_confirmation_box = (By.CSS_SELECTOR,".sweet-alert.showSweetAlert.visible")