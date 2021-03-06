'''Controller of Alt'r app'''
import sys

from models import SessionManager, CacheManager, ApiQuery, ChoiceMenu,\
                   Substitute, Category, UserHistory

CONFIG = {'username': 'off_admin',
          'password': 'goodfood',
          'api_scope': 1,
          'api_page_size': '1000',
          'api_link': 'https://fr.openfoodfacts.org/cgi/search.pl',
          'api_categories': ['aliments-et-boissons-a-base-de-vegetaux',
                             'boissons',
                             'plats-prepares',
                             'produits-laitiers',
                             'snacks-sucres',
                             'viandes'
                             ]
          }


def main(loop=True, sysarg=''):
    '''main function'''
    database = SessionManager(CONFIG['username'], CONFIG['password'])
    cache = CacheManager()
    if sysarg == "--commitcache":
        database.commit_cache(cache)
    if sysarg == "--fill":
        query = ApiQuery(CONFIG['api_scope'],
                         CONFIG['api_page_size'],
                         CONFIG['api_link'],
                         CONFIG['api_categories'])
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

PRIMARY_LOOP = True

while PRIMARY_LOOP:
    PRIMARY_LOOP = main()
