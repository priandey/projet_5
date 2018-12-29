import requests
import mysql.connector
import json

db_config = {
    'user' :'off_admin',
    'password' : 'goodfood',
    'host' : 'localhost',
    'database' : 'OpenFoodFacts'}
cnx = mysql.connector.connect(**db_config)
cursor = cnx.cursor()
#drop_table = ("DROP TABLE IF EXISTS nutrition_2;")
#create_table = ("CREATE TABLE nutrition_2(product_name VARCHAR(150) NOT NULL,nutrition_grades CHAR(1) NOT NULL, category_name VARCHAR(150) NOT NULL,product_id MEDIUMINT AUTO_INCREMENT NOT NULL PRIMARY KEY);")
#cursor.execute(drop_table)
#cursor.execute(create_table)
page = 1
#request_scope = int(input("Number of page you wish to ask (100 entry/page) :"))
#request_scope += 1
try:
    print("Looking for cached data")
    with open("resources/off_local_file.json", "r") as file:
        product_file = json.load(file)

except FileNotFoundError:
    while page < 5:
        str_page = str(page)
        print("Requesting page {}...".format(page))
        payload = {'action':'process',
                   'tagtype_0':'languages',
                   'tag_contains_0':'contains',
                   'tag_0':'fr',
                   'sort_by':'unique_scans_n',
                   'json':'1',
                   'page_size':'1000',
                   'page': str_page}
        page += 1
        brands = requests.get('https://fr.openfoodfacts.org/cgi/search.pl', params=payload)
        json_file = brands.json()

        print("Successfull API Request")

        with open("resources/off_local_file.json", "a") as file : #Need a debug
            json.dump(json_file,file)
        with open("resources/off_local_file.json", "r") as file:
            product_file = json.load(file)
        print("Request output saved to file")

for product in product_file['products']:
    try:
        add_product = ("INSERT INTO product "
                       "(product_name,nutrition_grade, product_category, product_url)"
                       "VALUES (%s, %s, %s, %s)")

        data_product = (product['product_name'], product['nutrition_grades'], product['categories_tags'][0][3:], product['url'])
        print("{} ({}), cat:{}, url: {}".format(product['product_name'], product['nutrition_grades'], product['categories_tags'][0][3:], product['url']))
        cursor.execute(add_product,data_product)
        cnx.commit()
    except KeyError:
        print("KeyError")
        continue

cursor.close()
cnx.close()
