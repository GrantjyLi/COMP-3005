
def test(cursor):
    q = f"insert into exercises (member_id, description) values (1, 'test')"
    cursor.execute(q)
    