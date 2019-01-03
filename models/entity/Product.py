from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    '''Mapped class of table product'''
    __tablename__ = 'product'
    product_name = Column(String)
    nutrition_grade = Column(String)
    product_url = Column(String, primary_key=True)
    category = relationship('models.entity.ProductCategory.ProductCategory', back_populates='product')
    def __repr__(self):
        return self.product_name
