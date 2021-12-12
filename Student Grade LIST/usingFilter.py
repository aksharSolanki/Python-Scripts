#Author : Akshar
#ID     : N01418888
#Date   : Nov 27, 2021

studentRecord = []

def takeInput():
    studentName = input("\nPlease enter the student's name: ")
    gradeMidterm = int(input("\nMidterm Grade: "))
    gradeFinal = int(input("\nFinal Grade: "))
    gradeAssign = int(input("\nAssignment Grade: "))
    saveStudentData(studentName, gradeMidterm, gradeFinal, gradeAssign)

def filterStudents(studentList):
    filtered_students = list(filter(lambda student: student[1] - 50 >= 0, studentList))
    print("\n--------------------------------------------------")
    print("List of filtered students who scored more than 50")
    for student in filtered_students:
        print("\nName: " + str(student[0]) + "\t|\t" + "Grade: " + str(student[1]))
    
def saveStudentData(name, midterm, final, assign):
    gradeTotal = (midterm + final + assign)
    gradeAvg = round((gradeTotal/3), 2)
    
    global studentRecord

    student = []
    student = [name, gradeTotal]
    studentRecord.append(student)
    showResult(name, gradeTotal, gradeAvg)
    filterStudents(studentRecord)

def showResult(studentName, gradeTotal, gradeAvg):
    print("\n--------------------------------------------------")
    print("Hi " + studentName + ". The total grade = " + str(gradeTotal) + ". Average = " + str(gradeAvg) + "%")
    print("\n--------------------------------------------------")
    print("List of all students registered: ")
    for student in studentRecord:
        print("\nName: " + str(student[0]) + "\t|\t" + "Grade: " + str(student[1]))

while(True):
    takeInput()
    print("\n--------------------------------------------------")
    res = input("Do you wish to enter another student? (y/n): ")
    if(res.lower() == "y"):
        print("\n<<<<<<<<Program is run again>>>>>>>>>")
    else:
        print("\nProgram is terminated")
        break
