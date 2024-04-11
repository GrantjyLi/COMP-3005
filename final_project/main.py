import psycopg2 # library to interact with postgresql
from Member_Interface import * 

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
    mid = login()

    name = getUserName(mid, "member", cursor)
    print("Welcome back " + name)

    choice = memberMenu()

    if choice ==1:
        updateUsername(mid, cursor)
    elif choice ==2:
        viewWeightGoal(mid, cursor)
    elif choice ==3:
        updateWeightGoal(mid, cursor)
    elif choice ==4:
        viewHealthMetrics(mid, cursor)
    elif choice ==5:
        addHealthMetric(mid, cursor)
    elif choice ==6:
        deleteHealthMetric(mid, cursor)
    elif choice ==7:
        viewGoals(mid, cursor)
    elif choice ==8:
        addGoal(mid, cursor)
    elif choice ==9:
        deleteGoal(mid, cursor)
    elif choice ==10:
        viewExercises(mid, cursor)
    elif choice ==11:
        addExercise(mid, cursor)
    elif choice ==12:
        deleteExercise(mid, cursor)
    elif choice ==13:
        viewAvailableSessions(cursor)
    elif choice ==14:
        viewPTSessions(mid)
    elif choice ==15:
        bookPTSession(mid, cursor)
    elif choice ==16:
        leavePTSession(mid, cursor)
    elif choice ==17:
        viewClasses(cursor)
    elif choice ==18:
        viewEnrolledClasses(mid, cursor)
    elif choice ==19:
        joinClass(mid, cursor)
    elif choice ==20:
        leaveClass(mid, cursor)


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

        while checkUser(mID, "member", cursor) == False:
            mID = int(input("Enter valid member ID#: "))
    else:
        username = input("Enter new username: ")
        weightGoal = int(input("Enter weight goal (lbs): "))
        goalDate = input("Enter weight goal date (yyyy-mm-dd): ")

        addMember(username, weightGoal, goalDate, cursor)
        mID = getUserID(username, "member", cursor)
    
    return mID

def memberMenu():
    print("Welcome to your Dashboard, here are your options:")
    print("1. Update Username\n")

    print("2. View Weight Goal")
    print("3. Update Weight Goal")

    print("4. View Health Metrics")
    print("5. Add Health Metric")
    print("6. Delete Health Metric\n")

    print("7. View Goals")
    print("8. Add Goals")
    print("9. Delete Goals\n")

    print("10. View Exercises")
    print("11. Add Exercise")
    print("12. Delete Exercise\n")

    print("13. View available PT-Sessions")
    print("14. View Your PT-Sessions")
    print("15. Book a PT-Session")
    print("16. Leave a PT-Session\n")

    print("17. View available Fitness Classes")
    print("18. View Your Fitness Classes")
    print("19. Join A Fitness Class")
    print("20. Leave a Fitness Class\n")

    choice =0
    while choice < 1 or choice > 21:
        choice = int(input("Enter a valid choice: "))

    return choice


control()

connection.commit()
cursor.close()
connection.close()