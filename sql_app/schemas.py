from typing import List, Optional

from pydantic import BaseModel, constr


class ItemBase(BaseModel):
    name: str
    price: float
    description: Optional[str] = None
    store_id: int
    group_id: int
    user_id:int

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
#group
class GroupBase(BaseModel):
    name: str


class GroupCreate(GroupBase):
    pass


class Group(GroupBase):
    id: int
    items: List[Item] = []

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
    email: str
    phone: int
    password: int
    role: str = 'user'
class UserCreate(UserBase):
    
    pass

class User(BaseModel):
    id: int
    email: str
    password: int
    class Config:
        orm_mode = True

class University(BaseModel):
    country: Optional[str] = None
    web_pages: List[str] = []
    name: Optional[str] = None
    alpha_two_code: Optional[str] = None
    domains: List[str] = []
