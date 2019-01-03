from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .Product import Product

Base = declarative_base()

class UserHistory(Base):
    '''Mapped class of table user_history'''
    __tablename__ = 'user_history'
    search_id = Column(Integer, primary_key=True)
    selected_product = Column(String, ForeignKey('product.product_url'))
    substitute = Column(String, ForeignKey('product.product_url'))
