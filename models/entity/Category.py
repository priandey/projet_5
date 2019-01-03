from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Category(Base):
    '''Mapped class of table category'''
    __tablename__ = 'category'
    category_name = Column(String, primary_key=True)
    product = relationship('models.entity.ProductCategory.ProductCategory', back_populates='category')

    def __repr__(self):
        return self.category_name
