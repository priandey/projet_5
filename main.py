from models import *

def main():
    database = SessionManager()
    #query = ApiQuery()
    #query.get_query()
    cache = CacheManager()
    database.commit_cache(cache)

    #database.products_of_cat()


main()
