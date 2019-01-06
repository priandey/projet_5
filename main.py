from models import *
import sys
import os

def main(sysarg=''):
    database = SessionManager()
    cache = CacheManager()
    if sysarg == "-commitcache":
        database.commit_cache(cache)
    if sysarg == "-fill":
        query = ApiQuery()
        query.get_query()
        database.commit_cache(cache)
    #Printing first menu
    #Printing menu of Category
    category_menu = ChoiceMenu(database.query(Category), first_panel=True)
    category_menu.navigate_list()
    #Printing menu of products
    product_menu = ChoiceMenu(database.cat_to_prod(category_menu.chosen_result))
    product_menu.navigate_list()
    #If user wish to go back to menu category, skipping substitute phase
    if not isinstance(product_menu.chosen_result, str):
        to_sub = Substitute(product_menu.chosen_result, database)
        to_sub.search_substitute()
        to_sub.print_substitute_menu()
    os.system('pause')


if len(sys.argv) > 1:
    main(sysarg=sys.argv[1])
while True:
    main()
