import psycopg2 # library to interact with postgresql
from cursortest import *
dbPW = "heying" #your postgresql password

connection = psycopg2.connect(host = "localhost", dbname = "Final_Project", user = "postgres", password = dbPW, port = "5432")
cursor = connection.cursor()


q = f"select * from members where username = 'm1'"
cursor.execute(q)
data = cursor.fetchall()

for m in data:
    print(f"Member ID#: {m[0]}")
    print(f"Member name: {m[1]}")
    print(f"Member Weight goal (lbs): {m[2]}")
    print(f"Member goal date: {m[3]}\n")

connection.commit()
cursor.close()
connection.close()