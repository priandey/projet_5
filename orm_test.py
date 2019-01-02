from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship



engine = create_engine('mysql+pymysql://off_admin:goodfood@localhost/OpenFoodFacts')
print(engine)

Base = declarative_base()

class Product(Base):
    __tablename__ = 'product'
    product_name = Column(String)
    nutrition_grade = Column(String)
    product_url = Column(String, primary_key=True)

#    def __repr__(self):
#        return "<Product(product_name='%s', nutrition_grade='%s', product_url='%s')>" % (self.product_name, self.nutrition_grade, self.product_url)

class Category(Base):
    __tablename__ = 'category'
    category_name = Column(String, primary_key=True)

class ProductCategory(Base):
    __tablename__ = 'product_category'
    id = Column(Integer, primary_key=True)
    product_url = Column(String, ForeignKey('product.product_url'))
    category_name = Column(String, ForeignKey('category.category_name'))

Session = sessionmaker(bind=engine)
session = Session()
produit = Product(product_name = "MAchin", nutrition_grade = "b", product_url = "http://trutouc.com/choubid/apimescouilles")

#session.add(produit)
#session.commit()

for category in session.query(Category):
    print(category.category_name)

print("\n{} categories found".format(session.query(Category).count()))
