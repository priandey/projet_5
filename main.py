from models import *
import sys

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
    first_menu = ChoiceMenu(['Chercher un produit', 'Parcourir mon historique de recherche'], first_panel=True)
    if first_menu.chosen_result == 'Chercher un produit':
        #Printing menu of Category
        category_menu = ChoiceMenu(database.query(Category), first_panel=True)
        #Printing menu of products
        product_menu = ChoiceMenu(database.cat_to_prod(category_menu.chosen_result))
        #If user wish to go back to menu category, skipping substitute phase
        if not isinstance(product_menu.chosen_result, str):
            to_sub = Substitute(product_menu.chosen_result, database)
            to_sub.search_substitute()
            to_sub.print_substitute_menu()
    elif first_menu.chosen_result == 'Parcourir mon historique de recherche':
        history_menu = ChoiceMenu(database.query(UserHistory))
        if not isinstance(history_menu.chosen_result, str):
            page = Substitute.substitute_from_userhistory(history_menu.chosen_result, database)
            page.print_substitute_menu()


if len(sys.argv) > 1:
    main(sysarg=sys.argv[1])
primary_loop = True
while primary_loop:
    main()
