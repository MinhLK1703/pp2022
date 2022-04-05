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
    def __init__(self, CName, CID):
        self.CourseName = CName
        self.CourseID = CID
    def show(self):
        print('CourseName is: ', self.CourseName)
        print('Course ID is: ', self.CourseID)

#Getting Number Of Student
def NumberOfStudent ():
    return int (input('Number of student: '))

#Getting Info Of Student    
def InfoOfStudent ():
    StudentName = input ('Student Name: ')
    StudentDOB = input ('Student DOB (DD/MM/YYYY): ')
    StudentID = input ('Student ID: ')
    return StudentName, StudentDOB, StudentID
#Getting Number Of Course    
def NumberOfCourse ():
    return int(input('Number of course: '))

#Getting Info Of Course
def InfoOfCourse ():
    CourseID = input('Course ID: ')
    CourseName = input('Course Name: ')
    CourseInfo = course(CourseName, CourseID)
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

#Listing all Students
def Listing_Students():
    for i in range (NoStudents):
        print("Student No ", i+1)
        print("Name/DOB/ID: ",studentList[i].StudentName, studentList[i].StudentDOB, studentList[i].StudentID)

#Creating List of Courses     
NoCourses = NumberOfCourse ()
courseList = []
for i in range (NoCourses):
    CourseID, CourseName = InfoOfCourse ()
    courseList.append ((CourseID, CourseName))

#Listing all Courses
def Listing_Courses():
    for i in range (NoCourses):
        print("Course No ", i+1)
        print("Name/ID: ",courseList[i].courseName, courseList[i].courseID)

#Mark n GPA unfinished
#Mark: for i in ListStudents, input Mark for i in ListCourses
#GPA: Variable Credits: Listing Courses; for i in ListCourses -> Input Credits
#