import psycopg2 # library to interact with postgresql
dbPW = "heying" #your postgresql password

connection = psycopg2.connect(host = "localhost", dbname = "Final_Project", user = "postgres", password = dbPW, port = "5432")
cursor = connection.cursor()


query = f"select member_names from fitness_classes"
cursor.execute(query)

out = cursor.fetchall()

for t in out:
    print(t[0][0])


connection.commit()
cursor.close()
connection.close()