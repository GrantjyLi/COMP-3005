#pip3 install psycopg2-binary
import psycopg2 # library to interact with postgresql
from queries import * # get functions that make queries

dbPW = "" #your postgresql password

#creating connection to local postgresql database and cursor to execute queries
connection = psycopg2.connect(host = "localhost", dbname = "a2-1", user = "postgres", password = dbPW, port = "5432")
cursor = connection.cursor()

#function to display options to user and get inputs
def control():
    initialize()

    while True:
        #displaying menu and then getting a valid input
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

        #if statment calls whatever function corresponding to user input
        #inputs are also collected for some functions
        if choice == 0:
            print("Exiting...")
            break

        elif choice ==1:
            menu1()

        elif choice ==2:
            fn = input("Enter first name: ")
            ln = input("Enter last name: ")
            em = input("Enter email: ")
            ed = input("Enter enrollment date (yyyy-mm-dd): ")
            menu2(fn, ln, em, ed)

        elif choice ==3:
            sid = int(input("Enter student Id: "))
            em = input("Enter updated email: ")
            menu3(sid, em)

        elif choice ==4:
            sid = int(input("Enter student Id: "))
            menu4(sid)

#function to initialize database if user wants to
def initialize():
    choice = "0" #getting valid user input
    while choice != "Y" and choice != "y" and choice != "N" and choice != "n":
        choice = input("Do you want to start from a clean table (y), or continue with last values (n): ")
    
    if choice == "Y" or choice == "y":
        global cursor
        #executes a query that creates a clean table with default data if user wants to
        cursor.execute(initQuery())   

#function to print out all students
def menu1():
    global cursor
    query = getAllStudents()
    cursor.execute(query)
    print("Students: ")
    for t in cursor.fetchall():
        print(t)

#function to add a student
def menu2(first_name, last_name, email, enrollment_date):
    global cursor
    query = addStudent(first_name, last_name, email, enrollment_date)
    cursor.execute(query)
    print("Student added")

#function to update student email
def menu3(student_id, new_email):
    global cursor
    query = updateStudentEmail(student_id, new_email)
    cursor.execute(query)
    print("Student email updated")

#function to delete student
def menu4(student_id):
    global cursor
    query = deleteStudent(student_id)
    cursor.execute(query)
    print("Student deleted")

#starting the control flow of the program
control()

#commiting to the database and closing tools when done
connection.commit()
cursor.close()
connection.close()