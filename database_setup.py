__author__ = 'fantom'

import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()
metadata = MetaData()


class Shop(Base):
    __tablename__ = 'shop'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Items(Base):
    __tablename__ = 'items'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    shop_id = Column(Integer, ForeignKey('shop.id'))
    shop = relationship(Shop, cascade="all, delete-orphan")

    @property
    def serialize(self):
        #Returns object data in easly serialized format
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course
        }

engine = create_engine('sqlite:///shopitems.db')
Base.metadata.create_all(engine)
