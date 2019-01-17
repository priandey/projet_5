'''Substitute Class'''
from random import choice

from colorama import init, Fore

from .entities import Product, ProductCategory, UserHistory
from .assets import ASSET


init(autoreset=True)


class Substitute():
    '''Object designed to get a substitute from the same category than a
       selected Product object, and print the result.'''
    def __init__(self, selected_product, session, origin=''):
        self.selected_product = selected_product
        self.substitute = self.selected_product
        self.session = session
        self.origin = origin

    @classmethod
    def substitute_from_userhistory(cls, history, database):
        '''Constructs a substitute object from a UserHistory object'''
        selected_product = []
        substitute = []

        for query_result in database.query(Product).\
                filter(Product.product_url == history.selected_product):
            selected_product = query_result

        for query_result in database.query(Product).\
                filter(Product.product_url == history.substitute):
            substitute = query_result

        substitute_object = cls(selected_product=selected_product,
                                session=database, origin='database')
        substitute_object.substitute = substitute

        return substitute_object

    def search_substitute(self):
        '''Search in the category of selected_product a product with a better
           nutrition grade. If product is already the best, the substitute will
           be the product itself by default'''
        all_substitute = []
        if self.selected_product.nutrition_grade == "a":
            pass
        else:
            for category in self.session.query(ProductCategory).\
                    join(Product).\
                    filter(ProductCategory.product_url ==
                           self.selected_product.product_url):
                for product in self.session.cat_to_prod(category):
                    all_substitute.append(product)

            all_substitute.sort(key=Substitute.get_product_grade)
            if len(all_substitute) > 1:
                all_substitute.remove(self.selected_product)
                final_index = round(len(all_substitute)/5)
                final_substitute = choice(all_substitute[0:final_index])
                self.substitute = final_substitute
            else:
                self.substitute = all_substitute[0]

    @classmethod
    def get_product_grade(cls, product):
        return product.nutrition_grade

    def print_substitute_menu(self):
        '''Print to the screen a str version of the substitute object'''
        ASSET.clear()
        print(ASSET.banner)
        if self.substitute.nutrition_grade >=\
           self.selected_product.nutrition_grade:
            print(f"Congrats ! You're already eating the best product"
                  "referenced in category!\n"
                  "See more details about it at "
                  f"{ASSET.green(self.selected_product.product_url)}\n"
                  f"Press <Enter> to leave this page")
            input()
        else:
            print(f"We found {ASSET.green(self.substitute.product_name)}"
                  " as a substitute for "
                  f"{ASSET.red(self.selected_product.product_name)} \n"
                  "The nutrition grade is "
                  f"{ASSET.green(self.substitute.nutrition_grade.upper())}"
                  f" while original product grade was "
                  f"{ASSET.red(self.selected_product.nutrition_grade.upper())}\n\n"
                  "Buy it at "
                  f"{ASSET.green(self.substitute.store + Fore.RESET)}\n\n"
                  "More information at : "
                  f"{ASSET.green(self.substitute.product_url)}\n\n")
            if self.origin == "database":
                print("Press <Enter> to leave this page")
                input()
            else:
                action = input("Press S to save search, "
                               "or press <Enter> to go to main menu\n>> ")
                if action.upper() == "S":
                    self.save_history()

    def save_history(self):
        '''save the substitute as a UserHistory object and
           commit it to database'''
        history = UserHistory(selected_product=self.selected_product.
                              product_url,
                              substitute=self.substitute.product_url)
        self.session.append(history)
        self.session.commit()
