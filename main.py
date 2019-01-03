from models import *

def main():
    database = SessionManager()
    cache = CacheManager()
    database.commit_cache(cache)

main()
