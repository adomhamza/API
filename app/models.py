from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    phone_number: int
    role_id: int = 0
    status: int = 1


class User(UserBase):
    pass


class ResponseUserModel(BaseModel):
    email: str
    first_name: str
    last_name: str
    phone_number: int
    created_at: datetime

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    name: str
    category_id: int
    amount: int
    inventory: int
    sold_count: int = 1
    description: Optional[str] = None


class Product(ProductBase):
    pass


class ResponseProductModel(ProductBase):
    product_id: int
    created_at: datetime

    class Config:
        orm_mode = True


# User Login

class UserLoginModel(BaseModel):
    email: EmailStr
    password: str
