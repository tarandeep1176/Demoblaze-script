from pydantic import BaseModel

class UserNameData(BaseModel):
    username : str

class PasswordData(BaseModel):
    password : str

class LoginData(BaseModel):
    UserNameData : UserNameData
    PasswordData : PasswordData