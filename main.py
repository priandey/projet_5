from models import SessionManager, CacheManager, ApiQuery, ChoiceMenu,\
                   Substitute, Category, UserHistory
import sys

CONFIG = {
          'username': 'off_admin',
          'password': 'goodfood'
          }


def main(loop=True, sysarg=''):
    database = SessionManager(CONFIG['username'], CONFIG['password'])
    cache = CacheManager()
    if sysarg == "--commitcache":
        database.commit_cache(cache)
    if sysarg == "--fill":
        query = ApiQuery()
        query.get_query()
        database.commit_cache(cache)
    # Printing first menu
    first_menu = ChoiceMenu(['Chercher un produit',
                             'Parcourir mon historique de recherche',
                             'Exit program'],
                            first_panel=True)

    if first_menu.chosen_result == 'Chercher un produit':
        # Printing menu of Category
        category_menu = ChoiceMenu(database.query(Category), first_panel=False)
        # Printing menu of products
        if not isinstance(category_menu.chosen_result, str):
            product_menu = ChoiceMenu(database.cat_to_prod
                                      (category_menu.chosen_result))
        # If user wish to go back to menu category, skipping substitute phase
            if not isinstance(product_menu.chosen_result, str):
                to_sub = Substitute(product_menu.chosen_result, database)
                to_sub.search_substitute()
                to_sub.print_substitute_menu()

    elif first_menu.chosen_result == 'Parcourir mon historique de recherche':
        history_menu = ChoiceMenu(database.query(UserHistory).
                                  order_by("created_at DESC"))
        if not isinstance(history_menu.chosen_result, str):
            page = Substitute.substitute_from_userhistory(history_menu.
                                                          chosen_result,
                                                          database)
            page.print_substitute_menu()
    elif first_menu.chosen_result == 'Exit program':
        loop = False
    return loop


if len(sys.argv) > 1:
    main(sysarg=sys.argv[1])

primary_loop = True

while primary_loop:
    primary_loop = main()
