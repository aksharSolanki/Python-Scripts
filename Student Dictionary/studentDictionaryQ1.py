
# AUTHOR: AKSHAR
# DATE: DECEMBER 09, 2021

studentInfo = {}
option = 0

def begin():
    print("\n**************| Main Menu |*****************")
def end():
    print("**********| Program Terminated |************\n")
    
# OPTION 1
def add_to_collection(name, grade1, grade2):
    name = name.upper()
    total = ((grade1 * 0.4) + (grade2 * 0.6))
    "{0:.2}".format(total)
    studentInfo[name] = total
    
def show_options():
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Find Student")
    print("4. Update Student Grade")
    print("5. View All Students")
    print("6. Display Top Grade and Lowest Grade")
    print("7. Save Transactions")
    print("8. Exit\n")
def get_student_name(action):
    studentName = input("Enter the student name: ")
    studentName = studentName.upper()
    action(studentName)
    
# OPTION 2
def delete_student(name):
    exists = name in studentInfo
    if(exists == True):
        deletedStudent = studentInfo.pop(name)
        print("Student deleted: " + name + "\t" + str(deletedStudent))
    else:
        print("Student does not exist")
        
# OPTION 3
def find_student(name):
    exists = name in studentInfo
    if(exists == True):
        grade = studentInfo[name]
        print("\nStudent name: " + name + "\tGrade: " + str(grade))
    else:
        print("\nStudent does not exist")
# OPTION 4
def update_student(name):
    exists = name in studentInfo
    if(exists == True):
        updatedMid = int(input("Enter the updated midterm grade: "))
        updatedFinal = int(input("Enter the updated final grade: "))
        add_to_collection(name, updatedMid, updatedFinal)
        print("Updated grade: " + str(studentInfo[name]) + " for student: " + name)
    else:
        print("Student does not exist")
# OPTION 5
def view_students():
    if(len(studentInfo) == 0):
        print("No students exist")
    for key, value in studentInfo.items():
        print("Student name: {0}\tGrade: {1}".format(key, value))
# OPTION 6
def top_students():
    if(len(studentInfo) == 0):
        print("No students exist")
    else:
        topGrade = 0
        minGrade = 100
        student_max = ""
        student_min = ""
        if(len(studentInfo) == 0):
            print("\nNo student exists in the record")
        else:
            for name, grade in studentInfo.items():
                if(grade > topGrade):
                    topGrade = grade
                    student_max = name
                
                if(grade < minGrade):
                    minGrade = grade
                    student_min = name
        print("\nStudent with max grades: " + student_max + "\t" + str(topGrade))
        print("Student with min grades: " + student_min + "\t" + str(minGrade))

def add_student():
    studentName = input("Please enter the student's name: ")
    midGrade = int(input("Please enter the Midterm grade: "))
    finalGrade = int(input("Please enter the Final grade: "))
    add_to_collection(studentName, midGrade, finalGrade)

# OPTION 7
def save_transactions():
    fileContent = ""
    try:
        file = open("studentTransactions.txt", "a+")
        for key, value in studentInfo.items():
            fileContent += ("Student name: {0}\tGrade: {1}".format(key, value))
        file.write(fileContent)
    except:
        print("Error occurred")
        raise
    finally:
        file.close()
    
try:
    while(option != 7):
        begin()
        show_options()
        option = int(input(":::"))
        if(option == 1):
            add_student()
        elif(option == 2):
            get_student_name(delete_student)
        elif(option == 3):
            get_student_name(find_student)
        elif(option == 4):
            get_student_name(update_student)
        elif(option == 5):
            print("\n--------------------------------------------")
            view_students()
            print("--------------------------------------------\n")
        elif(option == 6):
            top_students()
        elif(option == 7):
            save_transactions()
        elif(option == 8):
            end()
            break
        else:
            print("Error")
except(TypeError, ValueError):
    print("Please select one of the options")
finally:
    end()
