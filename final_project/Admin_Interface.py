def viewBookings(cursor):
    q = f"select * from room_bookings"
    cursor.execute(q)
    data = cursor.fetchall()

    for b in data:
        print(f"Booking ID#: {b[0]}")
        print(f"Room #: {b[1]}")
        print(f"Event Name: {b[2]}")
        print(f"Event date: {b[3]}\n")

def createBooking(cursor):
    roomNum = int(input("Room # for booking: "))
    bName = input("Booking name: ")
    date = input("Booking date (yyyy-mm-dd): ")
    q =f"insert into room_bookings (room_number, event_name, event_time) values ({roomNum}, '{bName}', '{date}')"
    
    cursor.execute(q)
    print("New Booking added\n")

def removeBooking(cursor):
    bid = int(input("Enter Booking ID#: "))
    q = f"delete from room_bookings where booking_id = {bid}"
    cursor.execute(q)
    print("Booking deleted\n")

def checkEquipment(cursor):
    q = f"select * from equipment"
    printEquipment(q, cursor)

def checkEquipmentID(cursor):
    eid = int(input("Enter equipment ID#: "))
    q = f"select * from equipment where equipment_id = {eid}"
    printEquipment(q, cursor)

def updateSchedules(cursor):
    bid = int(input("Enter the class ID# to update: "))
    date = input("New date (yyyy-mm-dd): ")

    q = f"update fitness_classes set class_time = '{date}' where class_id = {bid}"
    cursor.execute(q)
    print("Booking Time Updated\n")

def createBill(cursor):
    mid = int(input("Billing member ID#: "))
    amount = float(input("Bill amount $: "))
    date = input("Bill due date (yyyy-mm-dd): ")
    description = input("Bill Description: ")
    
    q = f"insert into billings (member_id, amount, bill_date, description) values ({mid}, {amount}, '{date}', '{description}')"
    cursor.execute(q)
    print("New Bill Created\n")


def printEquipment(query, cursor):
    cursor.execute(query)
    data = cursor.fetchall()

    for e in data:
        print(f"Equipment ID#: {e[0]}")
        print(f"Equipment name: {e[1]}")
        print(f"Equipment Maintenance Cost $: {e[2]}")
        print(f"Equipment Maintenance date: {e[3]}\n")