import psycopg2 # library to interact with postgresql
from Member_Interface import *
from Trainer_Interface import *
from Admin_Interface import *

dbPW = "" #your postgresql password
databasename = "Final_Project" # your postgresql database name 

connection = psycopg2.connect(host = "localhost", dbname = databasename, user = "postgres", password = dbPW, port = "5432")
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
    global cursor
    mid = memberLogin()

    name = getUserName(mid, "member", cursor)
    print("Welcome back " + name)

    printMemberMenu()
    while True:

        choice = -1 
        while choice < 0 or choice > 23:
            choice = int(input("Enter a valid choice: "))
    
        if choice ==0:
            print("Exiting Members menu\n")
            break
        elif choice ==1:
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
            viewPTSessions(mid, cursor)
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
        elif choice ==21:
            viewBills(mid, cursor)
        elif choice ==22:
            payBills(mid, cursor)
        else:
            printMemberMenu()

def trainerInterface():
    global cursor

    tid = -1
    while checkUser(tid, "trainer", cursor) == False:
        tid = int(input("Enter valid trainer ID#: "))

    cursor.execute(f"select username from trainers where trainer_id = {tid}")
    print(f"Welcome back {cursor.fetchone()[0]}\n")

    printTrainerMenu()

    while True:
        
        choice = -1 
        while choice < 0 or choice > 7:
            choice = int(input("Enter a valid choice: "))

        if choice ==0:
            print("Exiting Trainer Menu\n")
            return
        elif choice ==1:
            viewAllMembers(cursor)
        elif choice ==2:
            viewMembersID(cursor)
        elif choice ==3:
            viewMembersNames(cursor)
        elif choice ==4:
            viewMySessions(tid, cursor)
        elif choice ==5:
            addSession(tid, cursor)
        elif choice ==6:
            removeSession(tid, cursor)
        else:
            printTrainerMenu()

def adminInterface():
    global cursor

    aid = -1
    while checkUser(aid, "admin", cursor) == False:
        aid = int(input("Enter valid admin ID#: "))

    cursor.execute(f"select username from admins where admin_id = {aid}")
    print(f"Welcome back {cursor.fetchone()[0]}\n")

    printAdminMenu() 

    while True:
        
        choice = -1 
        while choice < 0 or choice > 9:
            choice = int(input("Enter a valid choice: ")) 
        
        if choice ==0:
            print("Exiting Admin Menu\n")
            return
        elif choice ==1:
            viewBookings(cursor)
        elif choice ==2:
            createBooking(cursor)
        elif choice ==3:
            removeBooking(cursor)
        elif choice ==4:
            checkEquipment(cursor)
        elif choice ==5:
            checkEquipmentID(cursor)
        elif choice ==6:
            viewClasses(cursor)
        elif choice ==7:
            updateSchedules(cursor)
        elif choice ==8:
            createBill(cursor)
        else:
            printAdminMenu()

def memberLogin():
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

def printMemberMenu():
    print("Welcome to your Dashboard, here are your options:\n")
    print("1. Update Username\n")

    print("2. View Weight Goal")
    print("3. Update Weight Goal\n")

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

    print("21. View Bills")
    print("22. Pay Bills\n")

    print("23. View Menu Again")
    print("0. Exit menu\n")

def printTrainerMenu():
    print("1. View All Member Profiles")
    print("2. View Member Profiles by ID#")
    print("3. View Member Profiles by Name")
    print("4. View Your session openings")
    print("5. Add Session Opening")
    print("6. Remove Session Opening")
    print("7. View Menu Again")
    print("0. Exit Trainer Menu\n")

def printAdminMenu():
    print("1, View All Bookings")
    print("2. Create New Room Booking")
    print("3. Remove Room Booking")
    print("4. Check All Equipment")
    print("5. Check Equipment by ID#")
    print("6. View Class Schedules")
    print("7. Update Class Schedules")
    print("8. Create Bill")
    print("9. View Menu Again")
    print("0. Exit Admin Menu\n")

control()

connection.commit()
cursor.close()
connection.close()