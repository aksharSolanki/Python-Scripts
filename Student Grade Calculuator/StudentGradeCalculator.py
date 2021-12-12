# AUTHOR: AKSHAR
# DATE: DEC 03, 2021

# STUDENT GRADE CALCULATOR

def calculateGrade(mid, final, assign):
    result = (mid * 0.3) + (final * 0.5) + (assign * 0.2)
    return result
    
while(True):
    studentName = input("\nEnter the student name: ")
    
    midterm = float(input("Enter your midterm grade: "))
    assert(midterm > 0), "Invalid grade"
    
    final = float(input("Enter your final grade: "))
    assert(final > 0), "Invalid grade"
    
    assignment = float(input("Enter your assignment grade: "))
    assert(assignment > 0), "Invalid grade"

    result = calculateGrade(midterm, final, assignment)

    print("Student result: " + str(result))

    resp = input("\nEnter 'y' to continue, 'n' to exit: ")
    if(resp == 'n'):
        break

    


    
