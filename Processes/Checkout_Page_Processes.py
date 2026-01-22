from Page_Functions.Checkout_Page_Functions import CheckoutPageFunctions
from Data.Checkout_Page_Data import CheckoutPageMother
class CheckoutPageProcess:

    def __init__(self, checkout:CheckoutPageFunctions):
        self.checkout = checkout

    def run_process(self):
        data = CheckoutPageMother().get()
        self.checkout.place_order(data.CheckoutData)
        self.checkout.get_order_details()

