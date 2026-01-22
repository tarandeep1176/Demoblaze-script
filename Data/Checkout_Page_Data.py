import dotenv
import os

from faker import Faker
from Models.Checkout_Model import CheckoutData, CheckoutDetails
fake = Faker()

class CheckoutPageMother:
    def __init__(self):
        dotenv.load_dotenv()
        self.fake = Faker()
        self.name = self.fake.name()
        self.country = self.fake.country()
        self.city = self.fake.city()
        self.credit_card_number = os.getenv("CREDIT_CARD_NUMBER")
        self.month = self.fake.month_name()
        self.year = self.fake.year()

    def get(self):
        return CheckoutDetails(
            CheckoutData = CheckoutData(
                name = self.name,
                country = self.country,
                city = self.city,
                credit_card_number = self.credit_card_number,
                month = self.month,
                year = int(self.year)
            )
        )