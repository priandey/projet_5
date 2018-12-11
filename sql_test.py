import mysql.connector

config = {
    'user' :'root',
    'password' : 'pitour',
    'host' : 'localhost',
    'database' : 'drop_test'
}

cnx = mysql.connector.connect(**config)



cnx.close()
