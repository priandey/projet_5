'''All classes processing data'''
import json
import os

import requests
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey, Column, Integer, String, Table
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

'''----------------------ORM Related Class-----------------------------------'''

Base = declarative_base()

'''PRODUCT_CATEGORY = Table('product_category', Base.metadata,
                         Column('product_url', ForeignKey('product.product_url'), primary_key=True),
                         Column('category_name', ForeignKey('category.category_name'),
                                primary_key=True)'''

class ProductCategory(Base):
    '''mapped class of table product_category'''
    __tablename__ = 'product_category'
    product_url = Column(String, ForeignKey('product.product_url'), primary_key=True)
    category_name = Column(String, ForeignKey('category.category_name'), primary_key=True)

    product = relationship('Product', back_populates='category')
    category = relationship('Category', back_populates='product')

    def __repr__(self):
        return '{} => {}'.format(self.product.product_name, self.category_name)

class Product(Base):
    '''Mapped class of table product'''
    __tablename__ = 'product'
    product_name = Column(String)
    nutrition_grade = Column(String)
    product_url = Column(String, primary_key=True)
    category = relationship('ProductCategory', back_populates='product')
    def __repr__(self):
        return self.product_name

class Category(Base):
    '''Mapped class of table category'''
    __tablename__ = 'category'
    category_name = Column(String, primary_key=True)
    product = relationship('ProductCategory', back_populates='category')

    def __repr__(self):
        return self.category_name

class UserHistory(Base):
    '''Mapped class of table user_history'''
    __tablename__ = 'user_history'
    search_id = Column(Integer, primary_key=True)
    selected_product = Column(String, ForeignKey('product.product_url'))
    substitute = Column(String, ForeignKey('product.product_url'))

class SessionManager():
    '''Instances of this class will hold an engine and a session binded to it,
    it can manage adding, committing and querying db'''

    def __init__(self, engine='mysql+pymysql://off_admin:goodfood@localhost/OpenFoodFacts'):
        self.engine = create_engine(engine)
        makesession = sessionmaker(bind=self.engine)
        self.session = makesession()

    def append(self, entry):
        self.session.add(entry)

    def commit(self):
        self.session.commit()

    def query(self, queried):
        output_list = list()
        for entry in self.session.query(queried):
            output_list.append(entry)
        return output_list

    def commit_cache(self, cache):
        if cache.assert_cache:
            all_category = list()
            product_category = list()
            product_incomplete = 0
            for product_file in cache.load_cache():
                for entry in product_file['products']:
                    try:
                        product = Product(product_name=entry['product_name'],
                                          nutrition_grade=entry['nutrition_grades'],
                                          product_url=entry['url']
                                          )
                        self.append(product)

                        for category in entry['categories_tags']:
                            #Saving tuple product/category for product_category table
                            to_add = ProductCategory(product_url=entry['url'],
                                                     category_name=category[3:].replace("-", " ")
                                                     .capitalize())
                            self.append(to_add)
                            if category[3:].replace("-", " ").capitalize() not in all_category:
                               all_category.append(category[3:].replace("-", " ").capitalize())
                    except KeyError:
                        product_incomplete += 1
                        continue

            for entry in all_category:
                category = Category(category_name=entry)
                self.append(category)
            self.commit()
            for product in self.query(Product):
                print("{}\n".format(product.category))


        else:
            print('No file in cache, please download data')

'''----------------------API Related Class-----------------------------------'''

class ApiQuery():
    '''Class managing API queries'''
    def __init__(self, scope=1, page_size='100',
                 api_link='https://fr.openfoodfacts.org/cgi/search.pl'):
        self.page = 1
        self.scope = scope
        self.page_size = page_size
        self.payload = {'action':'process',
                        'tagtype_0':'languages',
                        'tag_contains_0':'contains',
                        'tag_0':'fr',
                        'sort_by':'unique_scans_n',
                        'json':'1',
                        'page_size':self.page_size,
                        'page':str(self.page)}
        self.api_link = api_link

    def get_query(self, output_file="resources/off_p{}_local_file.json"):
        '''Request the API and dump result in a file
        Be sure to add {} in the output_file'''

        while self.page <= self.scope:
            print("Requesting page {}".format(self.page))
            raw_output = requests.get(self.api_link, params=self.payload)
            json_output = raw_output.json()
            self.page += 1

            with open(output_file.format(str(self.page)), "w") as file:
                json.dump(json_output, file)
            print("Request output dumped in file")

'''----------------------Cache Related Class-----------------------------------'''

class CacheManager():
    '''A cache manager'''
    def __init__(self, directory="resources/"):
        self.cache_dir = directory
        self.file_available = list()

    @property
    def assert_cache(self):
        '''Return a tuple (True, number_of_file_in_dir)
        if there is file in self.cache_dir ; else return False'''

        with os.scandir(self.cache_dir) as filelist:
            for entry in filelist:
                if entry.is_file():
                    if entry.name not in self.file_available:
                        self.file_available.append(entry.name)
        check = bool(self.file_available)

        return check

    def load_cache(self):
        '''Return a list of json dict object from self.cache_dir'''

        print("Loading cached files")
        files_output = list()
        for file in self.file_available:
            # print("{}{}".format(self.cache_dir, file))
            with open("{}{}".format(self.cache_dir, file), "r") as current_file:
                output = json.load(current_file)
                files_output.append(output)

        return files_output
