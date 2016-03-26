__author__ = 'fantom'

import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()
metadata = MetaData()


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    hasSub = Column(String(5))

    @property
    def serialize(self):
        # Returns object data in easily serialized format
        return {
            'id': self.id,
            'name': self.name,
            'hasSub': self.hasSub
        }


class SubCategory(Base):
    __tablename__ = 'sub_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    parentCat = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)

    @property
    def serialize(self):
        # Returns object data in easly serialized format
        return {
            'id': self.id,
            'name': self.name,
            'parentCat': self.category.id
        }


class ShopCategory(Base):
    __tablename__ = 'shop_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)


class Shop(Base):
    __tablename__ = 'shop'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    owner = Column(String(50), nullable=False)
    profile_pic = Column(String(200))
    avatar_pic = Column(String(200))
    description = Column(String(250))
    cat_id = Column(Integer, ForeignKey('shop_category.id'))
    category = relationship(ShopCategory)

    @property
    def serialize(self):
        # Returns object data in easly serialized format
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'owner': self.owner,
            'profile_pic': self.profile_pic
        }


class Items(Base):
    __tablename__ = 'items'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    short_description = Column(String(250))
    description = Column(String(500))
    quantity = Column(Integer, nullable=False)
    image = Column(String(20))
    price = Column(String(8))
    shop_id = Column(Integer, ForeignKey('shop.id'))
    shop = relationship(Shop, cascade="all, delete-orphan", single_parent=True)
    cat_id = Column(Integer, ForeignKey('sub_category.id'))
    SubCategory = relationship(SubCategory)

    @property
    def serialize(self):
        # Returns object data in easily serialized format
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'short_description': self.short_description,
            'shop_id': self.shop.id,
            'shop_name': self.shop.name,
            'cat_id': self.SubCategory.category.id,
            'sub_cat_id': self.SubCategory.id
        }


class ContactInfo(Base):
    __tablename__ = 'contact_info'
    id = Column(Integer, primary_key=True)
    email = Column(String(50))
    phone = Column(String(20))
    address = Column(String(150))
    shop_id = Column(Integer, ForeignKey('shop.id'))
    shop = relationship(Shop, cascade="all, delete-orphan", single_parent=True)


class PromoCode(Base):
    __tablename__ = 'promo_code'
    id = Column(Integer, primary_key=True)
    code = Column(String(150), nullable=False)
    shop_id = Column(Integer, ForeignKey('shop.id'))
    shop = relationship(Shop, cascade="all, delete-orphan", single_parent=True)


class ShopLocations(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    lon = Column(String(100), nullable=False)
    lat = Column(String(100), nullable=False)
    shop_id = Column(Integer, ForeignKey('shop.id'))
    shop = relationship(Shop, cascade="all, delete-orphan", single_parent=True)


class ItemPictures(Base):
    __tablename__ = 'item_pictures'
    id = Column(Integer, primary_key=True)
    url = Column(String(100), nullable=False)
    item_id = Column(Integer, ForeignKey('items.id'))
    item = relationship(Items, cascade="all, delete-orphan", single_parent=True)


class ItemVideo(Base):
    __tablename__ = 'item_video'
    id = Column(Integer, primary_key=True)
    url = Column(String(100), nullable=False)
    item_id = Column(Integer, ForeignKey('items.id'))
    item = relationship(Items, cascade="all, delete-orphan", single_parent=True)


class ItemReviews(Base):
    __tablename__ = 'item_reviews'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    star = Column(Integer, nullable=False)
    review = Column(String(500), nullable=False)
    item_id = Column(Integer, ForeignKey('items.id'))
    item = relationship(Items, cascade="all, delete-orphan", single_parent=True)


engine = create_engine('sqlite:///shopitems.db')
Base.metadata.create_all(engine)
