import psycopg2 # library to interact with postgresql
from cursortest import *
dbPW = "heying" #your postgresql password

connection = psycopg2.connect(host = "localhost", dbname = "Final_Project", user = "postgres", password = dbPW, port = "5432")
cursor = connection.cursor()

q = f"select bill_id, amount, bill_date, description from billings where member_id = {1}"
cursor.execute(q)
data = cursor.fetchall()

for b in data:
    print(f"Bill ID#: {b[0]}")
    print(f"Bill Amount: ${b[1]}")
    print(f"Bill date: {b[2]}")
    print(f"Bill description: {b[3]}\n")

connection.commit()
cursor.close()
connection.close()