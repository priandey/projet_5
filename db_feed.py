import requests
import mysql.connector
import json
import os

db_config = {
    'user' :'off_admin',
    'password' : 'goodfood',
    'host' : 'localhost',
    'database' : 'OpenFoodFacts'}
cnx = mysql.connector.connect(**db_config)
cursor = cnx.cursor()

page = 1

def assert_cache():
    file_available = list()
    with os.scandir("resources/") as filelist:
        for entry in filelist:
            if entry.is_file():
                file_available.append(entry.name)
    if len(file_available) == 0:
        return False
    else :
        return True, len(file_available)

def load_cache(dir):
    print("Loading cache files")
    file_available = list()
    files_output = list()
    with os.scandir(dir) as filelist:
        for entry in filelist:
            if entry.is_file():
                file_available.append(entry.name)
    for file in file_available:
        #print("{}{}".format(dir,file))
        with open("{}{}".format(dir,file), "r") as current_file:
            output = json.load(current_file)
            files_output.append(output)
    return files_output

if assert_cache()[0] is True :
    print("Looking for cached data")
    json_file_list = load_cache("resources/")

else :
    request_scope = int(input("Number of page you wish to ask (100 entry/page) :"))
    request_scope += 1
    while page <= request_scope:
        str_page = str(page)
        print("Requesting page {}...".format(page))
        payload = {'action':'process',
                   'tagtype_0':'languages',
                   'tag_contains_0':'contains',
                   'tag_0':'fr',
                   'sort_by':'unique_scans_n',
                   'json':'1',
                   'page_size':'100',
                   'page': str_page}
        page += 1
        brands = requests.get('https://fr.openfoodfacts.org/cgi/search.pl', params=payload)
        json_file = brands.json()

        print("Successfull API Request")

        with open("resources/off_p{}_local_file.json".format(str_page), "w") as file :
            json.dump(json_file,file)
        print("Request output dumped in cache file")

    json_file_list = load_cache("resources/")

all_category = list()
product_category = list()
product_incomplete = 0
print("Inserting {} products in db...".format(assert_cache()[1]*100))
for product_file in json_file_list:
    for product in product_file['products']:
        try:
            add_product = ("INSERT INTO product "
                           "(product_name,nutrition_grade, product_url)"
                           "VALUES (%s, %s, %s)")

            data_product = (product['product_name'], product['nutrition_grades'], product['url'])
            #print("{} ({}), url: {}".format(product['product_name'], product['nutrition_grades'], product['url']))
            cursor.execute(add_product,data_product)

            for category in product['categories_tags']: #Saving tuple product/category for product_category table
                product_category.append((product['url'],category[3:]))
                if category[3:] not in all_category:
                        all_category.append(category[3:])
        except KeyError:
            #print("<< Product incomplete >>")
            product_incomplete += 1
            continue

for category in all_category:
    #print(category)
    cursor.execute("INSERT INTO category (category_name) VALUES ('{}')".format(category))

for association in product_category :
    #print(association)
    cursor.execute("INSERT INTO product_category (product_url, category_name) VALUES ('{}', '{}')".format(association[0], association[1]))

print("{} products added to db \n{} products were not added to db. Cause : incomplete".format(assert_cache()[1]*100-product_incomplete,product_incomplete))

cnx.commit()
cursor.close()
cnx.close()
