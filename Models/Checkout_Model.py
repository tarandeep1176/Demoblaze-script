from pydantic import BaseModel

class CheckoutData(BaseModel):
    name : str
    country : str
    city : str
    credit_card_number : str
    month : str
    year : int

class CheckoutDetails(BaseModel):
    CheckoutData : CheckoutData