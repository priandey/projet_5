from models import *

def main():
    database = SessionManager()
    #query = ApiQuery()
    #query.get_query()
    #cache = CacheManager()
    #database.commit_cache(cache)

    choicemenu = ChoiceMenu(database.query(Product))
    choicemenu.navigate_list()
    #database.products_of_cat()


main()
