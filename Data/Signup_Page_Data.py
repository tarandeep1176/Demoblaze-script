import dotenv
import os
from Models.Signup_model import SignupData, UserNameData,PasswordData

class SignupPageMother:
    def __init__(self):
        dotenv.load_dotenv()
        self.app_username = os.getenv("APP_USERNAME")
        self.app_password = os.getenv("APP_PASSWORD")

    def get(self):
        return SignupData(
            UserNameData = UserNameData(username = self.app_username),
            PasswordData = PasswordData(password = self.app_password)
        )