def NumberOfStudent ():
    return int (input('Number of student: '))
    
def InfoOfStudent ():
    StudentID = input ('Student ID: ')
    StudentName = input ('Student Name: ')
    StudentDOB = input ('Student DOB (DD/MM/YYYY): ')
    return StudentID, StudentName, StudentDOB
    
def NumberOfCourse ():
    return int(input('Number of course: '))


def InfoOfCourse ():
    CourseID = input('Course ID: ')
    CourseName = input('Course Name: ')
    return CourseID, CourseName
    
def Mark (StudentID, CourseID):
    prompt = f"Student's mark {StudentID} for course {CourseID}; "
    input(prompt)

NoStudents = NumberOfStudent ()
studentList = []
for i in range (NoStudents):
    StudentID, StudentName, StudentDOB = InfoOfStudent ()
    studentList.append ((StudentID, StudentName, StudentDOB))
    
NoCourses = NumberOfCourse ()
courseList = []
for i in range (NoCourses):
    CourseID, CourseName = InfoOfCourse ()
    courseList.append ((CourseID, CourseName))
    
d = {}
n = int (input ('Number of student need correcting mark: '))
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
    Mark = int (input ('Mark: '))
    if CourseID in d:
        d [CourseID].append ((StudentID, Mark))
    else:
        d [CourseID] = [(StudentID, Mark)]