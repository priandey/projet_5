from .entities import Category, Product, ProductCategory, UserHistory
from .assets import ASSET
from random import choice

class Substitute():
    def __init__(self, selected_product, session, origin='search'):
        self.selected_product = selected_product
        self.substitute = []
        self.session = session
        self.origin = origin

    @classmethod
    def substitute_from_userhistory(cls, history, db):
        selected_product = []
        substitute = []
        for query_result in db.query(Product).filter(Product.product_url == history.selected_product):
            selected_product = query_result
        for query_result in db.query(Product).filter(Product.product_url == history.substitute):
            substitute = query_result
        substitute_object = cls(selected_product=selected_product, session=db, origin='db')
        substitute_object.substitute = substitute
        return substitute_object

    def search_substitute(self):
        all_substitute = []

        for category in self.session.query(ProductCategory).join(Product).\
                           filter(ProductCategory.product_url == self.selected_product.product_url):
            for product in self.session.cat_to_prod(category, substitute=True):
                all_substitute.append(product)

        all_substitute.sort(key=self.get_product_grade)
        self.substitute = all_substitute[0]

    def get_product_grade(self, product):
        return product.nutrition_grade

    def print_substitute_menu(self):
        ASSET.cls()
        print(ASSET.banner_2)
        if self.origin == 'search':
            print(f"\nWe found <{self.substitute}> as a substitute for <{self.selected_product}> \n"
                  f"The nutrition grade is <{self.substitute.nutrition_grade.upper()}>"
                  f" while original product grade was "
                  f"<{self.selected_product.nutrition_grade.upper()}> \n"
                  f"Buy it at {self.substitute.store}\n"
                  f"More information at : {self.substitute.product_url}")
            action = input("Press S to save search, or press <Enter> twice go to main menu")
            if action.upper() == "S":
                self.save_history()
        else :
            print(f"\nWe found <{self.substitute}> as a substitute for <{self.selected_product}> \n"
                  f"The nutrition grade is {self.substitute.nutrition_grade.upper()}"
                  f" while original product grade was "
                  f"{self.selected_product.nutrition_grade.upper()} \n"
                  f"Buy it at {self.substitute.store}\n"
                  f"More information at : {self.substitute.product_url}\n\n"
                  "Press <Enter> once to leave this page")
            input()


    def save_history(self):
        history = UserHistory(selected_product=self.selected_product.product_url,
                              substitute=self.substitute.product_url)
        self.session.append(history)
        self.session.commit()
        print(history)
