#*****THESE ARE FUNCTIONS THAT MAKE THE QUERIES THE a2-1.py USES

#returns a query that initializes the table and its data
def initQuery():
    initTable = """
create table students(
student_id serial primary key,
first_name text not null,
last_name text not null,
email text not null unique,
enrollment_date date
);
"""
    
    initData = """
INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
"""
    return f"""
drop table if exists students;
{initTable}
{initData}
"""

#function to print out all students
def getAllStudents():
    return """
    select * from students;
    """

#function to add a student
def addStudent(first_name, last_name, email, enrollment_date):
   
    return f"""
    insert into students (first_name, last_name, email, enrollment_date) values
    ('{first_name}', '{last_name}', '{email}', '{enrollment_date}');
    """

#function to update student email
def updateStudentEmail(student_id, new_email):
    return f"""
    update students
    set email = '{new_email}'
    where student_id = {student_id};
    """

#function to delete student
def deleteStudent(student_id):
    return f"""
    delete from students where student_id = {student_id};
    """