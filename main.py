import models as m

def main():
    database = m.SessionManager()
    cache = m.CacheManager()
    database.commit_cache(cache)

main()
