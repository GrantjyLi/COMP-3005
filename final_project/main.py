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
    choice = memberMenu()

    if choice ==1:

    elif choice ==2:
    elif choice ==3:
    elif choice ==4:
    elif choice ==5:
    elif choice ==6:
    elif choice ==7:
    elif choice ==8:
    elif choice ==9:
    elif choice ==10:
    elif choice ==11:
    elif choice ==12:
    elif choice ==13:
    elif choice ==14:
    elif choice ==15:
    elif choice ==16:
    elif choice ==17
    elif choice ==18:
    elif choice ==19:
    elif choice ==20:
    else:




    

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

def memberMenu():
    print("Welcome to your Dashboard, here are your options:")
    print("1. Update Username\n")

    print("2. View Weight Goal")
    print("3. Update Weight Goal")

    print("5. View Health Metrics")
    print("6. Add Health Metric")
    print("7. Delete Health Metric\n")

    print("8. View Goals")
    print("9. Add Goals")
    print("10. Delete Goals\n")

    print("11. View Exercises")
    print("12. Add Exercise")
    print("13. Delete Exercise\n")

    print("14. View available PT-Sessions")
    print("15. View Your PT-Sessions")
    print("16. Book a PT-Session")
    print("17. Leave a PT-Session\n")

    print("18. View available Fitness Classes")
    print("19. View Your Fitness Classes")
    print("20. Enter A Fitness Class")
    print("21. Leave a Fitness Class\n")

    choice =0
    while choice < 1 and choice > 21:
        choice = int(input("Enter a valid choice: "))

    return choice


control()

connection.commit()
cursor.close()
connection.close()