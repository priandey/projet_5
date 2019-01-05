from models import *

def main():
    database = SessionManager()
    #query = ApiQuery()
    #query.get_query()
    #cache = CacheManager()
    #database.commit_cache(cache)
    print(
            "                                         _|          \n"
            "             _|_|    _|    _|_|_|_|_|  _|    _|_|_|   \n"
            "           _|    _|  _|        _|            _|    _|  \n"
            "           _|_|_|_|  _|        _|            _|_|_|    \n"
            "           _|    _|  _|        _|            _|    _|  \n"
            "           _|    _|  _|_|_|_|  _|            _|    _|   \n"
            "         =============================================="
        )
    choicemenu = ChoiceMenu(database.query(Category))
    choicemenu.navigate_list()
    #database.products_of_cat()


main()
