from Libraries.Libraries import Import_libraries
from Data.Config_Data import ConfigData
from Page_Functions.Signup_Page_Functions import SignupPageFunctions
from Page_Functions.Login_Page_Functions import LoginPageFunctions
from Page_Functions.Phone_Page_Functions import PhonePageFunctions
from Page_Functions.Checkout_Page_Functions import CheckoutPageFunctions
from Page_Functions.Logout_Page_Functions import LogoutPageFunctions


from Processes.Signup_Page_Processes import SignupPageProcess
from Processes.Login_Page_Processes import LoginPageProcess
from Processes.Phone_Page_Processes import PhonePageProcess
from Processes.Checkout_Page_Processes import CheckoutPageProcess
from Processes.Logout_Page_Processes import LogoutPageProcess

data = ConfigData()
driver = Import_libraries.get_driver()
driver.get(data.BASE_URL)

signup_page_functions = SignupPageFunctions(driver)
login_page_functions = LoginPageFunctions(driver)
phone_page_functions = PhonePageFunctions(driver)
checkout_page_functions = CheckoutPageFunctions(driver)
logout_page_functions = LogoutPageFunctions(driver)

def test_signup():
    signup = SignupPageProcess(signup_page_functions)
    signup.run_process()

def test_login():
    login = LoginPageProcess(login_page_functions)
    login.run_process()

def test_Phone():
    phone = PhonePageProcess(phone_page_functions)
    phone.run_process()

def test_checkout():
    checkout = CheckoutPageProcess(checkout_page_functions)
    checkout.run_process()

def test_logout():
    logout = LogoutPageProcess(logout_page_functions)
    logout.run_process()
    driver.close()