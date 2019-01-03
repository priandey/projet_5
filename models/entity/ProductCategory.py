from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .Product import Product
from .Category import Category

Base = declarative_base()

class ProductCategory(Base):
    '''mapped class of table product_category'''
    __tablename__ = 'product_category'
    product_url = Column(String, ForeignKey('product.product_url'), primary_key=True)
    category_name = Column(String, ForeignKey('category.category_name'), primary_key=True)

    product = relationship('models.entity.Product.Product', back_populates='category')
    category = relationship('models.entity.Category.Category', back_populates='product')

    def __repr__(self):
        return '{} => {}'.format(self.product.product_name, self.category_name)
