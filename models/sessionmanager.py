from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .entities import Product, Category, ProductCategory, UserHistory

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
        return self.session.query(queried)

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
                    else :
                        appended_product.append(entry)
                    try:
                        product = Product(product_name=entry['product_name'],
                                          nutrition_grade=entry['nutrition_grades'],
                                          product_url=entry['url']
                                          )
                        self.append(product)

                        category = entry['categories_hierarchy'][0][3:].replace("-", " ")

                        product_category = ProductCategory(product_url=entry['url'],
                                                       category_name=category
                                                       .capitalize()
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
            self.commit()

        else:
            print('No file in cache, please download data')

    def products_of_cat(self):
        '''Retrieve all products from a specified category (cat)'''
        join_query = self.session.query(Category).all()
        for e in join_query:
            print(e.category_name, e.product.product_url)
