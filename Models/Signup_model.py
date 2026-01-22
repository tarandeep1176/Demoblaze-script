from pydantic import BaseModel

class UserNameData(BaseModel):
    username : str

class PasswordData(BaseModel):
    password : str

class SignupData(BaseModel):
    UserNameData : UserNameData
    PasswordData : PasswordData