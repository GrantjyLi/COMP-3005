
def test(cursor):
    cursor.execute("select * from goals where member_id = 1")
    print(cursor.fetchall())