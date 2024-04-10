def checkUser(uid, userType):
    return f"select exists (select * from {userType}s where {userType}_id={uid})"

def getUserName(uid, userType):
    return f"select * from {userType}s where {userType}_id={uid}"

def getUserID(username, userType):
    return f"select member_id from {userType}s where username = '{username}' order by {userType}_id desc limit 1"

def addMember(username, weightGoal, goadDate):
    return f"insert into members(username, weight_goal, time_goal) values ('{username}',{weightGoal},'{goadDate}')"
