import psycopg2 # library to interact with postgresql
from cursortest import *
dbPW = "heying" #your postgresql password

connection = psycopg2.connect(host = "localhost", dbname = "Final_Project", user = "postgres", password = dbPW, port = "5432")
cursor = connection.cursor()

bid = int(input("Pay which bill ID#: "))
date = input("What is the date of payment (yyyy-mm-dd): ")

q = f"select amount from billings where bill_id = {bid} and member_id = {2}"
cursor.execute(q)

cost =  cursor.fetchone()[0]

connection.commit()
cursor.close()
connection.close()