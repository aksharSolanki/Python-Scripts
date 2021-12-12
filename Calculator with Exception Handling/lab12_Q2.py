# AUTHOR: AKSHAR
# DATE: DEC 03, 2021

def begin():
    print("\n----------------------Program Started-----------------------")

def end():
    print("----------------------Good Bye " + userName + "-----------------------\n")

def divide(num1, num2):
    try:
        print ("Result: " + str(num1 / num2))
    except:
        print("An error occurred")
        raise
    finally:
        end()

def multiply(num1, num2):
   print ("Result: " + str(num1 * num2))

def add(num1, num2):
    print ("Result: " + str(num1 + num2))

def sub(num1, num2):
   print ("Result: " + str(num1 - num2))

def checkOperation(op, num1, num2):
    try:
        if(op == "/"):
            divide(num1, num2)
        elif(op == "*"):
            multiply(num1, num2)
        elif(op == "+"):
            add(num1, num2)
        else:
            sub(num1, num2)
    except:
        print("Error occurred")
        raise
    finally:
        end()
        
begin()
userName = input("Please enter your name: ")

options = "Enter the sign \nDivision(/) \nMultiplication(*) \nAddition(+) \nSubtraction(-)\n"

operation = input(options + ": ")

try:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
except:
    print("Error occurred")
    raise
finally:
    end()

checkOperation(operation, num1, num2)
 
end()
