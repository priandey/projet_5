import models as m

def main():
    db = m.SessionManager()
    result = db.query(m.Category)
    for entry in result:
        print(entry.category_name)

main()
