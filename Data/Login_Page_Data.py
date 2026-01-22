import dotenv
import os
from Models.Login_model import LoginData, UserNameData,PasswordData

class LoginPageMother:
    def __init__(self):
        dotenv.load_dotenv()
        self.app_username = os.getenv("APP_USERNAME")
        self.app_password = os.getenv("APP_PASSWORD")

    def get(self):
        return LoginData(
            UserNameData = UserNameData(username = self.app_username),
            PasswordData = PasswordData(password = self.app_password)
        )