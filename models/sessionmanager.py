'''Interface between DB and program. Uses sqlalchemy session.'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .entities import Product, Category, ProductCategory
from .substitute import Substitute as s

import os


class SessionManager():
    '''Instances of this class will hold an engine and a session binded to it,
    it can manage adding, committing and querying db'''

    def __init__(self, username, password):
        self.engine = create_engine(f'mysql+pymysql://{username}:{password}@localhost/OpenFoodFacts')
        makesession = sessionmaker(bind=self.engine)
        self.session = makesession()

    def append(self, entry):
        '''Add entry to queue'''
        self.session.add(entry)

    def commit(self):
        '''commit queue'''
        self.session.commit()

    def query(self, queried):
        '''return a list of entry from queried mapped object'''
        return self.session.query(queried)

    def cat_to_prod(self, category):
        '''for a Category object, retrieve all Product object related'''
        result = []
        for entry in self.query(ProductCategory).join(Category).\
                filter(Category.category_name == category.category_name):
            for entrance in self.query(Product).filter(Product.product_url
                                                       == entry.product_url):
                result.append(entrance)

        result.sort(key=s.get_product_grade, reverse=True)
        return result

    def commit_cache(self, cache):
        '''Upload cache-loaded content to db'''
        if cache.assert_cache:
            all_category = list()
            appended_product = list()
            product_incomplete = 0
            for product_file in cache.load_cache():
                for entry in product_file['products']:
                    if entry in appended_product:
                        continue
                    else:
                        appended_product.append(entry)
                    try:
                        if entry['stores'] == '':
                            continue
                        product = Product(product_name=entry['product_name'],
                                          nutrition_grade=entry['nutrition_grades'],
                                          product_url=entry['url'],
                                          store=entry['stores']
                                          )
                        self.append(product)

                        category = entry['categories_hierarchy'][0][3:].\
                            replace("-", " ").upper()

                        product_category = ProductCategory(product_url=entry['url'],
                                                           category_name=category
                                                           )
                        self.append(product_category)
                        if category not in all_category:
                            all_category.append(category)
                    except KeyError:
                        product_incomplete += 1
                        continue

            for entry in all_category:
                category = Category(category_name=entry)
                self.append(category)
            print("Committing to db...")
            print(f"{product_incomplete} products not committed because of missing informations")
            self.commit()
            os.system("pause")
        else:
            print('No file in cache, please download data')
