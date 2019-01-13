'''SQLalchemy models'''

from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Category(Base):
    '''Mapped class of table category'''
    __tablename__ = 'category'
    category_name = Column(String, primary_key=True)
    product = relationship('ProductCategory',
                           back_populates='category')

    def __repr__(self):
        return self.category_name


class Product(Base):
    '''Mapped class of table product'''
    __tablename__ = 'product'
    product_name = Column(String)
    nutrition_grade = Column(String)
    product_url = Column(String, primary_key=True, unique=True)
    store = Column(String)
    category = relationship('ProductCategory',
                            back_populates='product')

    def __repr__(self):
        return f'{self.product_name} ({self.nutrition_grade.upper()})'


class ProductCategory(Base):
    '''mapped class of table product_category'''
    __tablename__ = 'product_category'
    product_url = Column(String, ForeignKey('product.product_url'),
                         primary_key=True)
    category_name = Column(String, ForeignKey('category.category_name'),
                           primary_key=True)

    product = relationship('Product', back_populates='category')
    category = relationship('Category', back_populates='product')

    def __repr__(self):
        return self.product_url


class UserHistory(Base):
    '''Mapped class of table user_history'''
    __tablename__ = 'user_history'
    search_id = Column(Integer, primary_key=True)
    selected_product = Column(String, ForeignKey('product.product_url'))
    substitute = Column(String, ForeignKey('product.product_url'))
    created_at = Column(String, server_default="CURRENT_TIMESTAMP")
    selected_product_name = relationship('Product',
                                         foreign_keys=[selected_product])
    substitute_product_name = relationship('Product',
                                           foreign_keys=[substitute])

    def __repr__(self):
        return "{}\t| {} => {}".format(self.created_at,
                                      self.selected_product_name,
                                      self.substitute_product_name)
