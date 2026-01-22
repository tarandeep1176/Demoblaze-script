from Page_Functions.Phone_Page_Functions import PhonePageFunctions

class PhonePageProcess:

    def __init__(self, phone:PhonePageFunctions):
        self.phone = phone

    def run_process(self):
        self.phone.add_to_cart()
        self.phone.open_cart_page()

