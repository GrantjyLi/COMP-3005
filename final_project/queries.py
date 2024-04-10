def checkUser(uid, userType):
    return f"select exists (select * from {userType}s where {userType}_id={uid})"

def getUserName(uid, userType):
    return f"select * from {userType}s where {userType}_id={uid}"

def getUserID(username, userType):
    return f"select member_id from {userType}s where username = '{username}' order by {userType}_id desc limit 1"

def addMember(username, weightGoal, goadDate):
    return f"insert into members(username, weight_goal, time_goal) values ('{username}',{weightGoal},'{goadDate}')"

def updateUsername(uid):
    newName = input("Enter new username: ")
    return f"update members set username = '{newName}' where member_id = {uid}"

def viewWeightGoal(uid):
    return f"select weight_goal, time_goal from members where member_id = {uid}"

def updateWeightGoal(uid):
    newWeight = int(input("Enter new Weight goal (lbs): "))
    newDate = input("Enter new weight goal date (yyyy-mm-dd): ")
    return f"update members set weight_goal = {newWeight}, time_goal = {newDate} where member_id = {uid}"

def viewHealthMetrics(uid):
    return f"select metric_type, metric_value, date_measured from health_metrics where member_id = {uid}"

def addHealthMetric(uid):
    newMType = input("Enter new metric type: ")
    metricVal = int(input("Enter new metric value: "))
    newDate = input("Enter date for new metric (yyyy-mm-dd): ")
    return f"insert into health_metrics(member_id, metric_type, metric_value, date_measured) values ({uid}, '{newMType}', {metricVal}, '{newDate}')"

def deleteHealthMetric(uid):
    mid = input("Enter the ID for a health metric")
    return f"delete from health_metrics where (metric_id = {mid} and member_id = {uid})"

def 