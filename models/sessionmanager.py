from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .entity import *

class SessionManager():
    '''Instances of this class will hold an engine and a session binded to it,
    it can manage adding, committing and querying db'''

    def __init__(self, engine='mysql+pymysql://off_admin:goodfood@localhost/OpenFoodFacts'):
        self.engine = create_engine(engine)
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
        output_list = list()
        for entry in self.session.query(queried):
            output_list.append(entry)
        return output_list

    def commit_cache(self, cache):
        '''Upload cache-loaded content to db'''
        if cache.assert_cache:
            all_category = list()
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
                            product_category = ProductCategory(product_url=entry['url'],
                                                     category_name=category[3:].replace("-", " ")
                                                     .capitalize())
                            self.append(product_category)
                            if category[3:].replace("-", " ").capitalize() not in all_category:
                                all_category.append(category[3:].replace("-", " ").capitalize())
                    except KeyError:
                        product_incomplete += 1
                        continue

            for entry in all_category:
                category = Category(category_name=entry)
                self.append(category)
            self.commit()

        else:
            print('No file in cache, please download data')
