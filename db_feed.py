import requests
import mysql.connector

db_config = {
    'user' :'root',
    'password' : 'pitour',
    'host' : 'localhost',
    'database' : 'drop_test'}
cnx = mysql.connector.connect(**db_config)
cursor = cnx.cursor()
page = 1
while True:
    print(page)
    str_page = str(page)
    page += 1
    try:
        payload = {'action':'process',
                   'tagtype_0':'languages',
                   'tag_contains_0':'contains',
                   'tag_0':'fr',
                   'sort_by':'unique_scans_n',
                   'json':'1',
                   'page_size':'1000',
                   'page': str_page}
        brands = requests.get('https://fr.openfoodfacts.org/cgi/search.pl', params=payload)
        json = brands.json()



        for i in json['products']:
            try:
                add_product = ("INSERT INTO nutrition "
                               "(product_name,nutrition_grades)"
                               "VALUES (%s, %s)")

                data_product = (i['product_name'], i['nutrition_grades'])

                cursor.execute(add_product,data_product)
                cnx.commit()
            except KeyError:
                print("KeyError")
                continue
    except:
        break

cursor.close()
cnx.close()
