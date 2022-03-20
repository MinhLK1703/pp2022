def getStudentCount ():
    return int (input ("No. of students: "))
    
def getCourseCount ():
    return int (input ("No. of courses: "))
    
def getCourseInfo ():
    cid = input ("Course's id: ")
    cname = input ("Course's name: ")
    return cid, cname
    
def getStudentInfo ():
    sid = input ("Student's ID: ")
    sname = input ("Student Name: ")
    sdob = input ("Student DOB: ")
    return sid, sname, sdob
    
def getMarks (sid, cid):
    prompt = f"Student's marks {sid} for course {cid}: ".format (sid, cid)
    input (prompt)
    
nStudents = getStudentCount ()
studentList = []
for i in range (nStudents):
    sid, nm, dob = getStudentInfo ()
    studentList.append ((sid, nm, dob))

nCourses = getCourseCount ()
courseList = []
for i in range (nCourses):
    cid, cname = getCourseInfo ()
    courseList.append ((cid, cname))
    
d = {}    
n = int (input ("No. of Student-course marks: "))
for i in range (n):
    while True:
        sid = input ("Student ID: ")
        cid = input ("Course ID: ")
        if sid not in [student [0] for student in studentList]:
            print ("Wrong Student ID")
            continue 
        if cid not in [course [0] for course in courseList]:
            print ("Wrong Student ID")
            continue 
        break
    marks = int (input ("Marks: "))
    if cid in d:
        d [cid].append ((sid, marks))
    else:
        d [cid] = [(sid, marks)]
        
print ("\nListing all students...")
for s in studentList:
    print (f"Student ID: {s[0]} Name: {s[1]} DOB: {s[2]}")

print ("\nListing all courses...")
for c in courseList:
    print (f"Course ID: {c[0]} Name: {c[1]}")
    
cid = input ("\nAll Student Markk for Course? ")
if cid in d:
    for tups in d [cid]:
        print (f"Student {tups[0]} got {tups [1]} marks")