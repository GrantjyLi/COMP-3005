def viewAllMembers(cursor):
    q = f"select * from members"
    printMembers(q, cursor)

def viewMembersID(cursor):
    mid = int(input("Enter member ID#: "))
    q = f"select * from members where member_id = {mid} limit 1"
    printMembers(q, cursor)

def viewMembersNames(cursor):
    name = input("Enter member name: ")
    q = f"select * from members where username = '{name}'"
    printMembers(q, cursor)

def addSession(tid, cursor):
    newDate = input("Enter new session date (yyyy-mm-dd): ")
    q = f"insert into availabilities (trainer_id, available_time) values ({tid}, '{newDate}')"
    cursor.execute(q)
    print("New Session added\n")

def removeSession(tid, cursor):
    sid = int(input("Enter the ID for a session: "))
    q = f"delete from availabilities where (session_id = {sid} and trainer_id = {tid})"
    cursor.execute(q)
    print("Session removed\n")

def printMembers(query, cursor):
    cursor.execute(query)
    data = cursor.fetchall()

    for m in data:
        print(f"Member ID#: {m[0]}")
        print(f"Member name: {m[1]}")
        print(f"Member Weight goal (lbs): {m[2]}")
        print(f"Member goal date: {m[3]}\n")