import psycopg2

connection = psycopg2.connect(
    dbname="social", user="postgres", password="Mlkgw1", host="localhost")
cursor = connection.cursor()
