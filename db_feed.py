import requests
import mysql.connector

db_config = {
    'user' :'root',
    'password' : 'pitour',
    'host' : 'localhost',
    'database' : 'drop_test'}
cnx = mysql.connector.connect(**db_config)
cursor = cnx.cursor()
drop_table = ("DROP TABLE IF EXISTS nutrition_2;")
create_table = ("CREATE TABLE nutrition_2(product_name VARCHAR(150) NOT NULL,nutrition_grades CHAR(1) NOT NULL, category_name VARCHAR(150) NOT NULL,product_id MEDIUMINT AUTO_INCREMENT NOT NULL PRIMARY KEY);")
cursor.execute(drop_table)
cursor.execute(create_table)
page = 1
request_scope = int(input("Number of page you wish to ask (100 entry/page) :"))
while page < 7:
    print(page)
    str_page = str(page)
    page += 1
    #try:
    payload = {'action':'process',
               'tagtype_0':'languages',
               'tag_contains_0':'contains',
               'tag_0':'fr',
               'sort_by':'unique_scans_n',
               'json':'1',
               'page_size':'100',
               'page': str_page}
    brands = requests.get('https://fr.openfoodfacts.org/cgi/search.pl', params=payload)
    json = brands.json()



    for i in json['products']:
        try:
            add_product = ("INSERT INTO nutrition_2 "
                           "(product_name,nutrition_grades, category_name)"
                           "VALUES (%s, %s, %s)")

            data_product = (i['product_name'], i['nutrition_grades'], i["categories_tags"][1][3:])

            cursor.execute(add_product,data_product)
            cnx.commit()
        except KeyError:
            print("KeyError")
            continue
    #except:
    #    print("Error in API request")
    #    break

cursor.close()
cnx.close()
