from models import *
import os

def main():
    database = SessionManager()
    #query = ApiQuery()
    #query.get_query()
    #cache = CacheManager()
    #database.commit_cache(cache)

    category_menu = ChoiceMenu(database.query(Category), first_panel=True)
    category_menu.navigate_list()
    product_menu = ChoiceMenu(database.cat_to_prod(category_menu.chosen_result))
    product_menu.navigate_list()
    #database.products_of_cat()

while True:
    main()
