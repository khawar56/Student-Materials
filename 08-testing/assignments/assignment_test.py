import pytest 
import Student
import System
import json
import Staff
import Professor 

def test_login():
    checkStudent = System.System()
    name = "akend3"
    password = "123454321"
    password = "123"
    checkStudent.login(name,password)
    with open('Data/users.json') as f:
        data = json.load(f)
    
    if name not in data:
        assert False
            
            
def test_password():
    name = "akend3"
    password = "123454321"
    #when entered different password like the comment below, assertion is raised 
    #password = "123"
    checkPassword = System.System()
    result = checkPassword.check_password(name,password)
    if not result:
        assert False

#testing wrong password                 
def test_password_fail(): #fail test
    name = "akend3"
    password = "xyz"
    #when entered different password like the comment below, assertion is raised 
    #password = "123"
    checkPassword = System.System()
    result = checkPassword.check_password(name,password)
    if not result:
        assert False
        
        
#testing wrong username                 
def test_username_fail(): #fail test
    name = "khawar"
    password = "xyz"
    #when entered different password like the comment below, assertion is raised 
    #password = "123"
    checkPassword = System.System()
    result = checkPassword.check_password(name,password)
    if not result:
        assert False

def test_change_grade():
    name = "akend3"
    course = "comp_sci"
    assignment = "assignment1"
    g = 10
    changeGrade = Staff.Staff()
    changeGrade.change_grade(name, course, assignment,g)
    
    with open('Data/users.json') as f:
        data = json.load(f)
        #self.users[user]['courses'][course][assignment]['grade'] = 0
        grade = data["akend3"]['courses']["comp_sci"]["assignment1"]["grade"]
    if grade == 0:
        assert True
    else:
        assert False    
        
##changing grade of a user that does not exisit 
def test_change_grade_fail(): ##fail test
    name = "khawar"
    course = "someCourse"
    assignment = "assignmentXYZ"
    g = 10
    changeGrade = Staff.Staff()
    changeGrade.change_grade(name, course, assignment,g)
    
    with open('Data/users.json') as f:
        data = json.load(f)
        #self.users[user]['courses'][course][assignment]['grade'] = 0
        grade = data["khawar"]['courses']["someCourse"]["assignment1"]["grade"]
    if grade == 0:
        assert True
    else:
        assert False  

def test_create_assignment(): ##fail
    assignment_name = "meh"
    due_date = "never mind"
    course = "bruh"
    create_Assignment = Staff.Staff()
    create_Assignment.create_assignment(assignment_name, due_date, course)
    
    with open('Data/courses.json') as f:
        data = json.load(f)
    if course in data:
        assert True
    else:
        assert False    
    
    
def test_add_student(): ##fail
    name = "khawar"
    course = "comp_sci"
    
    with open('Data/courses.json') as f:
        all_courses = json.load(f)
        
    with open('Data/users.json') as f:
        all_users = json.load(f)
            
    add_student = Professor.Professor(name,all_users,all_courses)
    add_student.add_student(name,course)
    
    with open('Data/users.json') as f:
        users = json.load(f)
    
    if name in users:
        assert True    
    else:
        assert False     
    
    
def test_drop_student():
    ##drops user name if it exists in the DB
    ##if not, it drops 
    name = "akend3"    
    course = "comp_sci"
    
    with open('Data/courses.json') as f:
        all_courses = json.load(f)
        
    with open('Data/users.json') as f:
        all_users = json.load(f)
        
    drop_student = Professor.Professor(name,all_users,all_courses)
    drop_student.add_student(name,course)  
    
    with open('Data/users.json') as f:
        users = json.load(f)
    
    if name in users:
        assert True    
    else:
        assert False 
        
##dropping student which does not exist 
def test_drop_student_fail(): #fail
    name = "khawar"    
    course = "someCourse"
    
    with open('Data/courses.json') as f:
        all_courses = json.load(f)
        
    with open('Data/users.json') as f:
        all_users = json.load(f)
        
    drop_student = Professor.Professor(name,all_users,all_courses)
    drop_student.add_student(name,course)  
    
    with open('Data/users.json') as f:
        users = json.load(f)
    
    if name in users:
        assert True    
    else:
        assert False         
        
def test_submit_assignment(): ##fail 
    name = "akend3"    
    course = "comp_sci"
    
    with open('Data/courses.json') as f:
        all_courses = json.load(f)
        
    with open('Data/users.json') as f:
        all_users = json.load(f)
        
    submit_assignment = Student.Student(name,all_users,all_courses)
    submission_date = 14
    submission = "Test submission" 
    assignment_name = "test_assignment"
    submit_assignment.submit_assignment(course,assignment_name,submission,submission_date)
    
    with open('Data/courses.json') as f:
        courses = json.load(f)
    
    
    #self.all_courses['comp_sci']['assignments'][assignment_name]["due_date"]
    if courses[course]['assignments'][assignment_name][submission_date]:
        assert True
    else:
        assert False    
    


def test_submission_on_time(): 
    name = "akend3"    
    with open('Data/courses.json') as f:
        all_courses = json.load(f)
        
    with open('Data/users.json') as f:
        all_users = json.load(f)
    on_time = Student.Student(name,all_users,all_courses)
    submission_date = ""
    due_date = ""
    
    if on_time.check_ontime(submission_date,due_date):
        assert True
    else:
        assert False
        
##incorrect user name testing
def test_submission_on_time_fail():  ##fail 
    name = "khawar"    
    with open('Data/courses.json') as f:
        all_courses = json.load(f)
        
    with open('Data/users.json') as f:
        all_users = json.load(f)
    on_time = Student.Student(name,all_users,all_courses)
    submission_date = ""
    due_date = ""
    
    if on_time.check_ontime(submission_date,due_date):
        assert True
    else:
        assert False        
        
def test_check_grades():  ##fail
    name = "akend3"    
    course = "comp_sci"
    with open('Data/courses.json') as f:
        all_courses = json.load(f)
        
    with open('Data/users.json') as f:
        all_users = json.load(f)
    check = Student.Student(name,all_users,all_courses)
    grades = check.check_grades(course)
    
    if grades:
        #can also check if correct grades are return for correct student 
        assert True
    else:
        assert False    

def test_view_assignments(): ##fail 
    name = "akend3"    
    course = "comp_sci"
    with open('Data/courses.json') as f:
        all_courses = json.load(f)
        
    with open('Data/users.json') as f:
        all_users = json.load(f)
    check = Student.Student(name,all_users,all_courses)
    assignments_returned = check.view_assignments(course)
    
    with open('Data/courses.json') as f:
        courses_data = json.load(f)
    
    course = data['comp_sci']['assignments']
    assignments = []
    for key in course:
        assignments.append([key,course[key]['due_date']])
    
    if assignments_returned == assignments:
        #can also check if correct assignments are returned
        assert True
    else:
        assert False   



       
# @pytest.fixture
# def login_check():
#     checkStudent = System.System()
#     checkStudent.login()
#     return checkStudent