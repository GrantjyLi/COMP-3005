#pip3 install psycopg2-binary
import psycopg2
import os
from init import initQuery

#getting database password
dbPW = os.getenv("databasePW")

#creating connection to local postgresql database and cursor to execute queries
connection = psycopg2.connect(host = "localhost", dbname = "a2-1", user = "postgres", password = dbPW, port = "5432")
cursor = connection.cursor()

#function to display options to user and get inputs
def control():
    initialize()

    choice = -1
    while choice != 0:
        print("\nMenu:")
        print("1) Get all students.")
        print("2) Add a student.")
        print("3) Update a student's email.")
        print("4) Delete a student.")
        print("0) Exit.")

        choice = -1
        while choice < 0 or choice > 4:
            choice = int(input("Enter menu input: "))
        
        print("")
        if choice == 0:
            print("Exiting...")
            break

        elif choice ==1:
            getAllStudents()

        elif choice ==2:
            fn = input("Enter first name: ")
            ln = input("Enter last name: ")
            em = input("Enter email: ")
            ed = input("Enter enrollment date (yyyy-mm-dd): ")
            addStudent(fn, ln, em, ed)

        elif choice ==3:
            sid = int(input("Enter student Id: "))
            em = input("Enter updated email: ")
            updateStudentEmail(sid, em)

        elif choice ==4:
            sid = int(input("Enter student Id: "))
            deleteStudent(sid)

#function to initialize database if user wants to
def initialize():
    choice = "0"
    while choice != "Y" and choice != "y" and choice != "N" and choice != "n":
        choice = input("Do you want to start from a clean table (y), or continue with last values (n): ")
    
    if choice == "Y" or choice == "y":
        global cursor
        cursor.execute(initQuery())   

#function to print out all students
def getAllStudents():
    global cursor
    query = """
    select * from students;
    """

    cursor.execute(query)
    for t in cursor.fetchall():
        print(t)

#function to add a student
def addStudent(first_name, last_name, email, enrollment_date):
    global cursor
    query = f"""
    insert into students (first_name, last_name, email, enrollment_date) values
    ('{first_name}', '{last_name}', '{email}', '{enrollment_date}');
    """
    #building a query with parameters and then executing it
    cursor.execute(query)
    print("Student added")

#function to update student email
def updateStudentEmail(student_id, new_email):
    global cursor
    query = f"""
    update students
    set email = '{new_email}'
    where student_id = {student_id};
    """

    cursor.execute(query)
    print("Student email updated")

#function to delete student
def deleteStudent(student_id):
    global cursor
    query = f"""
    delete from students where student_id = {student_id};
    """

    cursor.execute(query)
    print("Student deleted")

#starting the control flow of the program
control()

#commiting to the database and closing tools when done
connection.commit()
cursor.close()
connection.close()