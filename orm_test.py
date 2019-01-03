from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy import Table, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('mysql+pymysql://off_admin:goodfood@localhost/OpenFoodFacts')
print(engine)

Base = declarative_base()

product_category = Table('product_category', Base.metadata,
                    Column('product_url', ForeignKey('product.product_url'), primary_key=True),
                    Column('category_name', ForeignKey('category.category_name'), primary_key=True)
                    )

class Product(Base):
    __tablename__ = 'product'
    product_name = Column(String)
    nutrition_grade = Column(String)
    product_url = Column(String, primary_key=True)
    category = relationship('Category',
                            secondary = product_category,
                            back_populates='product')
    def __repr__(self):
        return self.product_name
#    def __repr__(self):
#        return "<Product(product_name='%s', nutrition_grade='%s', product_url='%s')>" % (self.product_name, self.nutrition_grade, self.product_url)

class Category(Base):
    __tablename__ = 'category'
    category_name = Column(String, primary_key=True)
    product = relationship('Product',
                            secondary = product_category,
                            back_populates='category')
    def __repr__(self):
        return self.category_name

'''class ProductCategory(Base):
    __tablename__ = 'product_category'
    id = Column(Integer, primary_key=True)
    product_url = Column(String, ForeignKey('product.product_url'))
    category_name = Column(String, ForeignKey('category.category_name'))'''

class UserHistory(Base):
    __tablename__ = 'user_history'
    search_id = Column(Integer, primary_key=True)
    selected_product = Column(String, ForeignKey('product.product_url'))
    substitute = Column(String, ForeignKey('product.product_url'))

Session = sessionmaker(bind=engine)
session = Session()
#produit = Product(product_name = "Bidule", nutrition_grade = "b", product_url = "http://trutouc.com/choubidoubidou/")
#session.add(produit)


#session.commit()

for category in session.query(Category):
    print("{} ===> {} \n".format(category.category_name, category.product))

print("\n{} categories found".format(session.query(Product).count()))
