from typing import List, Optional

from pydantic import BaseModel ,EmailStr


class ItemBase(BaseModel):
    name: str
    price: float
    description: Optional[str] = None
    store_id: int
    user_id: int


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True


class StoreBase(BaseModel):
    name: str


class StoreCreate(StoreBase):
    pass


class Store(StoreBase):
    id: int
    items: List[Item] = []

    class Config:
        orm_mode = True
#user
class UserBase(BaseModel):
    name: str
    email: str
    password: int
    phone: int

class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    items: List[Item] = []

    class Config:
        orm_mode = True

class UserRegister(BaseModel):
    name: str

