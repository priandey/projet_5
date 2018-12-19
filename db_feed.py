import requests
import mysql.connector

db_config = {
    'user' :'root',
    'password' : 'pitour',
    'host' : 'localhost',
    'database' : 'drop_test'}

payload = {'search_terms':'biscuit',
           'search_simple':'1',
           'page_size':'120',
           'json':'1',
           'complete':'1'}
brands = requests.get('https://fr.openfoodfacts.org/cgi/search.pl', params=payload)
json = brands.json()

cnx = mysql.connector.connect(**db_config)
cursor = cnx.cursor()

for i in json['products']:
    try:
        add_product = ("INSERT INTO nutrition "
                       "(product_name,nutrition_grades)"
                       "VALUES (%s, %s)")

        data_product = (i['product_name'], i['nutrition_grades'])

        cursor.execute(add_product,data_product)
        cnx.commit()
    except KeyError:
        continue

cursor.close()
cnx.close()
