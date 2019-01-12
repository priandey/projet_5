from .entities import Category, Product, ProductCategory, UserHistory
from .assets import ASSET
from random import choice
from colorama import init, Fore, Back
init(autoreset=True)

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
            if not len(all_substitute) ==  1:
                all_substitute.remove(self.selected_product)
                final_substitute = choice(all_substitute[0:round(len(all_substitute)/5)])
                self.substitute = final_substitute
            else :
                self.substitute = all_substitute[0]


    @classmethod
    def get_product_grade(cls, product):
        return product.nutrition_grade

    def print_substitute_menu(self):
        ASSET.cls()
        print(ASSET.banner_2)
        if self.substitute.nutrition_grade >= self.selected_product.nutrition_grade:
            print(f"Congrats ! You're already eating the best product referenced in category!\n"
                  f"See more details about it at {Fore.GREEN + self.selected_product.product_url + Fore.RESET}\n"
                  f"Press <Enter> to leave this page")
            input()
        else:
            print(f"\nWe found <{Fore.GREEN + self.substitute.product_name + Fore.RESET}>"
                  f" as a substitute for <{Fore.RED + self.selected_product.product_name + Fore.RESET}> \n\n"
                  f"The nutrition grade is {Fore.GREEN + self.substitute.nutrition_grade.upper() + Fore.RESET}"
                  f" while original product grade was "
                  f"{Fore.RED + self.selected_product.nutrition_grade.upper() + Fore.RESET} \n\n"
                  f"Buy it at {Fore.GREEN + self.substitute.store + Fore.RESET}\n\n"
                  f"More information at : {Fore.GREEN + self.substitute.product_url + Fore.RESET}\n\n")
            if self.origin == "db":
                print("Press <Enter> to leave this page")
                input()
            else :
                action = input("Press S to save search, or press <Enter> to go to main menu\n>>  ")
                if action.upper() == "S":
                    self.save_history()


    def save_history(self):
        history = UserHistory(selected_product=self.selected_product.product_url,
                              substitute=self.substitute.product_url)
        self.session.append(history)
        self.session.commit()
        print(history)
