import psycopg2 # library to interact with postgresql
from queries import * 

dbPW = "heying" #your postgresql password

connection = psycopg2.connect(host = "localhost", dbname = "Final_Project", user = "postgres", password = dbPW, port = "5432")
cursor = connection.cursor()

def control():
    print("Welcome to the Health and Fitness club management system")
    print("Select a login option:")
    print("1. member")
    print("2. trainer")
    print("3. administrator")
    choice = 0

    while choice != 1 and choice != 2 and choice != 3:
        choice = int(input("Enter a valid choice: "))

    print("")
    if choice == 1:
        memberInterface()
    elif choice == 2:
        trainerInterface()
    else:
        adminInterface()
    
    print("closing program...")

def memberInterface():
    mId = login()

    




    



    

# def trainerInterface():
# def adminInterface():

def login():
    print("1. login as existing member")
    print("2. become new member")
    choice = 0

    while choice != 1 and choice != 2:
        choice = int(input("Enter valid choice: "))
    
    mID = -1
    if choice == 1:
        cursor.execute(checkUser(mID, "member"))

        while cursor.fetchone()[0] == False:
            mID = int(input("Enter valid member ID#: "))
            cursor.execute(checkUser(mID, "member"))

        cursor.execute(getUserName(mID, "member"))

        print("Welcome back " + cursor.fetchone()[1])
    else:
        username = input("Enter new username: ")
        weightGoal = int(input("Enter weight goal (lbs): "))
        goalDate = input("Enter weight goal date (yyyy-mm-dd): ")

        cursor.execute(addMember(username, weightGoal, goalDate))
        cursor.execute(getUserID(username, "member"))

        mID = cursor.fetchone()[0]
    
    return mID

control()

connection.commit()
cursor.close()
connection.close()