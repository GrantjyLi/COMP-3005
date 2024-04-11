def checkUser(uid, userType, cursor):
    q = f"select exists (select * from {userType}s where {userType}_id={uid})"
    cursor.execute(q)
    return cursor.fetchone()[0]

def getUserName(uid, userType, cursor):
    q = f"select username from {userType}s where {userType}_id={uid}"
    cursor.execute(q)
    return cursor.fetchone()[0]

def getUserID(username, userType, cursor):
    q = f"select {userType}_id from {userType}s where username = '{username}' order by {userType}_id desc limit 1"
    cursor.execute(q)
    return cursor.fetchone()[0]

def addMember(username, weightGoal, goadDate, cursor):
    q = f"insert into members(username, weight_goal, time_goal) values ('{username}',{weightGoal},'{goadDate}')"
    cursor.execute(q)
    print("Profile added\n")

def updateUsername(uid, cursor):
    newName = input("Enter new username: ")
    q =  f"update members set username = '{newName}' where member_id = {uid}"
    cursor.execute(q)
    print("Username updated\n")

def viewWeightGoal(uid, cursor):
    q = f"select weight_goal, time_goal from members where member_id = {uid}"
    cursor.execute(q)
    data = cursor.fetchone()
    print(f"Weight goal: {data[0]}")
    print(f"Goal date: {data[1]}\n")

def updateWeightGoal(uid, cursor):
    newWeight = int(input("Enter new Weight goal (lbs): "))
    newDate = input("Enter new weight goal date (yyyy-mm-dd): ")
    q = f"update members set weight_goal = {newWeight}, time_goal = '{newDate}' where member_id = {uid}"
    cursor.execute(q)
    print("Weight goal updated\n")

def viewHealthMetrics(uid, cursor):
    q = f"select metric_id, metric_type, metric_value, date_measured from health_metrics where member_id = {uid}"
    cursor.execute(q)
    for i in cursor.fetchall():
        print(f"metric ID#: {i[0]}")
        print(f"metric unit: {i[1]}")
        print(f"metric value: {i[2]}")
        print(f"metric date: {i[3]}\n")

def addHealthMetric(uid, cursor):
    newMType = input("Enter new metric type: ")
    metricVal = int(input("Enter new metric value: "))
    newDate = input("Enter date for new metric (yyyy-mm-dd): ")
    q = f"insert into health_metrics(member_id, metric_type, metric_value, date_measured) values ({uid}, '{newMType}', {metricVal}, '{newDate}')"
    cursor.execute(q)
    print("New metric added\n")

def deleteHealthMetric(uid, cursor):
    mid = int(input("Enter the ID for a health metric: "))
    q = f"delete from health_metrics where (metric_id = {mid} and member_id = {uid})"
    cursor.execute(q)
    print("Metric deleted\n")

def viewGoals(uid, cursor):
    q = f"select * from goals where member_id = {uid}"
    cursor.execute(q)
    for i in cursor.fetchall():
        print(f"Goal ID#: {i[0]}")
        print(f"Goal description: {i[2]}\n")

def addGoal(uid, cursor):
    description = input("Enter new goal description: ")
    q = f"insert into goals (member_id, description) values ({uid}, '{description}')"
    cursor.execute(q)
    print("Goal added")

def deleteGoal(uid, cursor):
    gid = int(input("Enter the ID for a goal: "))
    q = f"delete from goals where (goal_id = {gid} and member_id = {uid})"
    cursor.execute(q)
    print("Goal deleted")

def viewExercises(uid, cursor):
    q = f"select * from exercises where member_id = {uid}"
    cursor.execute(q)
    for i in cursor.fetchall():
        print(f"Exercise ID#: {i[0]}")
        print(f"Exercise Name: {i[2]}\n")

def addExercise(uid, cursor):
    eName = input("Enter exercise name: ")
    q = f"insert into exercises (member_id, description) values ({uid}, '{eName}')"
    cursor.execute(q)
    print("Exercise added\n")

def deleteExercise(uid, cursor):
    eid = int(input("Enter the ID for an exercise: "))
    q = f"delete from exercises where (exercise_id = {eid} and member_id = {uid})"
    cursor.execute(q)
    print("Exercise removed\n")

def viewAvailableSessions(cursor):
    q = f"select * from availabilities"
    cursor.execute(q)
    for i in cursor.fetchall():
        print(f"Slot ID#: {i[0]}")
        print(f"trainer ID#: {i[1]}")
        print(f"Slot date: {i[2]}\n")

def viewPTSessions(uid, cursor):
    q = f"select session_id, trainer_id, session_time from pt_sessions where member_id = {uid}"
    cursor.execute(q)
    for i in cursor.fetchall():
        print(f"Session ID#: {i[0]}")
        print(f"trainer ID#: {i[1]}")
        print(f"Session date: {i[2]}\n")

def bookPTSession(uid, cursor):
    sid = int(input("Enter the availability ID#: "))

    q = f"select * from availabilities where session_id = {sid} limit 1"
    cursor.execute(q)
    data = cursor.fetchone()

    if data[0] == None:
        print("This session is not available")
        return
    else:
        q = f"delete from availabilities where session_id = {sid}"
        cursor.execute(q)
        trainerID = data[1]
        time = data[2]

        q = f"insert into pt_sessions (trainer_id, member_id, session_time) values ({trainerID}, {uid}, '{time}')"
        cursor.execute(q)

        print("new session added\n")


def leavePTSession(uid, cursor): 
    sid = int(input("Enter the session ID#: "))
    q = f"select trainer_id, session_time from pt_sessions where session_id = {sid} and member_id = {uid} limit 1"
    cursor.execute(q)
    data = cursor.fetchone()

    if data[0] != None:
        q = f"delete from pt_sessions where session_id = {sid} and member_id = {uid}"
        cursor.execute(q)
        trainerID = data[0]
        time = data[1]

        q = f"insert into availabilities (trainer_id, available_time) values ({trainerID}, '{time}')"
        cursor.execute(q)

    print("Session removed\n")

def viewClasses(cursor):
    q = f"select class_id, class_name, trainer_id, class_time from fitness_classes"
    cursor.execute(q)
    for i in cursor.fetchall():
        print(f"Class ID#: {i[0]}")
        print(f"Class Name: {i[1]}")
        print(f"trainer ID#: {i[2]}")
        print(f"Class date: {i[3]}\n")

def viewEnrolledClasses(uid, cursor):
    q = f"select class_id, class_name, trainer_id, class_time from fitness_classes where {uid} = any (member_ids)"
    cursor.execute(q)
    for i in cursor.fetchall():
        print(f"Class ID#: {i[0]}")
        print(f"Class Name: {i[1]}")
        print(f"trainer ID#: {i[2]}")
        print(f"Class date: {i[3]}\n")

def joinClass(uid, cursor):
    cid = int(input("What is the class ID# you want to join: "))
    q = f"update fitness_classes set member_ids = array_append(member_ids, {uid}) where class_id = {cid}"
    cursor.execute(q)
    print(f"You joined class {cid}")

def leaveClass(uid, cursor):
    cid = int(input("What is the class ID# you want to leave: "))
    q = f"update fitness_classes set member_ids = array_remove(member_ids, {uid}) where class_id = {cid}"
    cursor.execute(q)
    print(f"You left class {cid}")

def viewBills(uid, cursor):
    q = f"select bill_id, amount, bill_date, description from billings where member_id = {uid}"
    cursor.execute(q)
    data = cursor.fetchall()

    for b in data:
        print(f"Bill ID#: {b[0]}")
        print(f"Bill Amount: ${b[1]}")
        print(f"Bill date: {b[2]}")
        print(f"Bill description: {b[3]}\n")

def payBills(uid, cursor):
    bid = int(input("Pay which bill ID#: "))
    date = input("What is the date of payment (yyyy-mm-dd): ")

    q = f"select amount from billings where bill_id = {bid} and member_id = {uid}"
    cursor.execute(q)

    cost = cursor.fetchone()[0]

    q = f"delete from billings where bill_id = {bid} and member_id = {uid}"
    cursor.execute(q)

    q = f"insert into payments(member_id, amount, payment_date) values({uid}, {cost}, '{date}')"
    cursor.execute(q)
    print("Bill payed\n")
