class person:
    def __init__(self, Name, DOB):
        self.PersonName = Name
        self.PersonDOB = DOB
    def show(self):
        print('Person name is: ', self.Name)
        print('Person DOB is: ', self.DOB)
class student:
    def __init__(self, Name, DOB, ID):
        self.StudentName = Name
        self.StudentDOB = DOB
        self.StudentID = ID
    def show(self):
        print('Student name is: ', self.StudentName)
        print('Student DOB is: ', self.StudentDOB)
        print('Student ID is: ', self.StudentID)
class course():
    def __init__(self, Name, ID):
        self.CourseName = Name
        self.CourseID = ID
    def show(self):
        print('CourseName is: ', self.CourseName)
        print('Course ID is: ', self.CourseID)

#Getting Number Of Student
def NumberOfStudent ():
    return int (input('Number of student: '))

#Getting Info Of Student    
def InfoOfStudent (self):
    StudentName = input ('Student Name: ')
    StudentDOB = input ('Student DOB (DD/MM/YYYY): ')
    StudentID = input ('Student ID: ')
    return StudentName, StudentDOB, StudentID,
#Getting Number Of Course    
def NumberOfCourse ():
    return int(input('Number of course: '))

#Getting Info Of Course
def InfoOfCourse ():
    CourseID = input('Course ID: ')
    CourseName = input('Course Name: ')
    CourseInfo = course(Name, ID)
    return CourseID, CourseName, CourseInfo
    
def Mark (StudentID, CourseID):
    prompt = f"Student's mark {StudentID} for course {CourseID}; "
    input(prompt)

#Creating List of Students
NoStudents = NumberOfStudent ()
studentList = []
for i in range (NoStudents):
    StudentID, StudentName, StudentDOB = InfoOfStudent ()
    studentList.append ((StudentID, StudentName, StudentDOB))

#Creating List of Courses     
NoCourses = NumberOfCourse ()
courseList = []
for i in range (NoCourses):
    CourseID, CourseName = InfoOfCourse ()
    courseList.append ((CourseID, CourseName))

#Define the Number and Who need correcting mark   
d = {}
n = int (input ('No. of student need correcting mark: '))
for i in range (n):
    while True:
        StudentID = input ('Student ID: ')
        CourseID = input ('CourseID: ')
        if StudentID not in [student [0] for student in studentList]:
            print ('Invalid Student ID')
            continue
        if CourseID not in [course [0] for course in courseList]:
            print ('Invalid Course ID')
            continue
        break
#Input Mark
    Mark = int (input ('Mark: '))
    if CourseID in d:
        d [CourseID].append ((StudentID, Mark))
    else:
        d [CourseID] = [(StudentID, Mark)]