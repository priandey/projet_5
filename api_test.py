import requests
import mysql.connector

db_config = {
    'user' :'root',
    'password' : 'pitour',
    'host' : 'localhost',
    'database' : 'drop_test'}

payload = {'search_terms':'salad',
           'search_simple':'1',
           'page_size':'120',
           'json':'1',
           'complete':'1',
           'nutrition_grades':'a'}
brands = requests.get('https://fr.openfoodfacts.org/cgi/search.pl', params=payload)
json = brands.json()

cnx = mysql.connector.connect(**db_config)
cursor = cnx.cursor()

for i in json['products']:
    add_product = ("INSERT INTO nutrition "
                   "(product_name,nutrition_grades)"
                   "VALUES (%s, %s)")

    data_product = (i['product_name'], i['nutrition_grades'])

    cursor.execute(add_product,data_product)
    cnx.commit()

cursor.close()
cnx.close()
