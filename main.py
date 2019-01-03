import models as m

def main():
    db = m.SessionManager()
    cache = m.CacheManager()
    db.commit_cache(cache)

main()
