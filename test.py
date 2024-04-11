import psycopg2 # library to interact with postgresql
from cursortest import *
dbPW = "heying" #your postgresql password

connection = psycopg2.connect(host = "localhost", dbname = "Final_Project", user = "postgres", password = dbPW, port = "5432")
cursor = connection.cursor()


#test(cursor)

mid = 1
sid = int(input("Enter the session ID#: "))

q = f"select trainer_id, session_time from pt_sessions where session_id = {sid} and member_id = {mid} limit 1"
cursor.execute(q)
data = cursor.fetchone()

if data[0] != None:
    q = f"delete from pt_sessions where session_id = {sid} and member_id = {mid}"
    cursor.execute(q)
    trainerID = data[0]
    time = data[1]

    q = f"insert into availabilities (trainer_id, available_time) values ({trainerID}, '{time}')"
    cursor.execute(q)

print("Session removed\n")


connection.commit()
cursor.close()
connection.close()