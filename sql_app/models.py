from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from db import Base
    
class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True,index=True)
    user_id = Column(Integer,ForeignKey('users.id'),nullable=True)
    name = Column(String(80), nullable=False, unique=True,index=True)
    group_id = Column(Integer,ForeignKey('groups.id'),nullable=True)
    price = Column(Float(precision=2), nullable=False)
    description = Column(String(200))
    store_id = Column(Integer,ForeignKey('stores.id'),nullable=False)
    

    
class Store(Base):
    __tablename__ = "stores"
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(80), nullable=False, unique=True)
    items = relationship("Item",primaryjoin="Store.id == Item.store_id",cascade="all, delete-orphan")


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(100), nullable=False, unique=True)
    items = relationship("Item",primaryjoin="Group.id == Item.group_id",cascade="all, delete-orphan")

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False,index=True)
    name = Column(String,  nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    phone = Column(Integer, nullable=True)
    role = Column(String, server_default='user', nullable=False)
    items = relationship("Item",primaryjoin="User.id == Item.user_id",cascade="all, delete-orphan")