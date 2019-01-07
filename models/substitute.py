from .entities import Category, Product, ProductCategory, UserHistory
from .assets import ASSET
from random import choice

class Substitute():
    def __init__(self, selected_product, session, origin=''):
        self.selected_product = selected_product
        self.substitute = self.selected_product
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
        if self.selected_product.nutrition_grade == "a":
            self.origin = 'perfect'
        else:
            for category in self.session.query(ProductCategory).join(Product).\
                               filter(ProductCategory.product_url == self.selected_product.product_url):
                for product in self.session.cat_to_prod(category):
                    all_substitute.append(product)

            all_substitute.sort(key=Substitute.get_product_grade)
            all_substitute.remove(self.selected_product)
            final_substitute = choice(all_substitute[0:round(len(all_substitute)/5)])
            self.substitute = final_substitute


    @classmethod
    def get_product_grade(cls, product):
        return product.nutrition_grade

    def print_substitute_menu(self):
        ASSET.cls()
        print(ASSET.banner_2)
        if self.substitute.nutrition_grade >= self.selected_product.nutrition_grade:
            print(f"Congrats ! You're already eating the best product !\n"
                  f"See more details about it at {self.selected_product.product_url}\n"
                  f"Press <Enter> to leave this page"
                  )
            input()
        elif self.origin == 'db' :
            print(f"\nWe found <{self.substitute.product_name}> as a substitute for <{self.selected_product.product_name}> \n"
                  f"The nutrition grade is {self.substitute.nutrition_grade.upper()}"
                  f" while original product grade was "
                  f"{self.selected_product.nutrition_grade.upper()} \n"
                  f"Buy it at {self.substitute.store}\n"
                  f"More information at : {self.substitute.product_url}\n\n"
                  "Press <Enter> to leave this page")
            input()
        else :
            print(f"\nWe found <{self.substitute.product_name}> as a substitute for <{self.selected_product.product_name}> \n"
                  f"The nutrition grade is <{self.substitute.nutrition_grade.upper()}>"
                  f" while original product grade was "
                  f"<{self.selected_product.nutrition_grade.upper()}> \n"
                  f"Buy it at {self.substitute.store}\n"
                  f"More information at : {self.substitute.product_url}")
            action = input("Press S to save search, or press <Enter> to go to main menu\n>>  ")
            if action.upper() == "S":
                self.save_history()


    def save_history(self):
        history = UserHistory(selected_product=self.selected_product.product_url,
                              substitute=self.substitute.product_url)
        self.session.append(history)
        self.session.commit()
        print(history)
