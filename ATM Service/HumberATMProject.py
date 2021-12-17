

userPin = None
trial = 1
option = None
file = None
count = 0
balance = 0
account = {}

def validate(pin):
    global file
    global account
    global balance
    global count
    
    file = open("HumberATM.txt", "r")
    for lines in file.readlines():
        if str(pin) in lines:
            account['PIN:'] = pin
            split = lines.split()
            balance = int(split[3])
            account['BALANCE:'] = balance
            return True
        else:
            return False

def openAccount():
    global option
    print("\nPlease press 1 for your balance")
    print("\nPlease press 2 to make a withdrawal")
    print("\nPlease press 3 to deposit fund")
    print("\nPlease press 4 to return card\n")
    option = int(input("Please make your selection >> "))
    checkOption(option)

def checkOption(option):
    global file
    global balance
    global account
    global userPin
    
    if(option == 1):
        print("\nYour balance is: $" + str(account['BALANCE:']))
        
    if(option == 2):
        print("\nEnter the amount you would like to withdraw")
        print("$10")
        print("$20")
        print("$40")
        print("$60")
        print("$80")
        print("$100")
        withdrawAmount = float(input("For other enter 1 >> "))
        if(withdrawAmount == 1):
            amount = float(input("Enter the amount to be withdrawn >> "))
            if(amount < balance):
                balance = (balance - withdrawAmount)
                account['BALANCE:'] = balance
                print("\nYour balance is now $" + str(account['BALANCE:']))
            else:
                print("Insufficient funds in the account")
        elif(withdrawAmount == 10 or withdrawAmount == 20 or withdrawAmount == 40 or
             withdrawAmount == 60 or withdrawAmount == 80 or withdrawAmount == 100):
            if(balance >= withdrawAmount):
                balance = (balance - withdrawAmount)
                account["BALANCE:"] = balance
                print("\nYour balance is now $" + str(account["BALANCE:"]))
            else:
                print("Insufficient funds in the account")
        else:
            print("Invalid amount. Please try again")
                
    if(option == 3):
        depositAmount = float(input("How much would you like to deposit >> "))
        if(depositAmount > 0):
            balance = (balance + depositAmount)
            account["BALANCE:"] = balance
        else:
            print("Please enter valid amount")
            
    if(option == 4):
        print("Please wait whilst your card is returned...")
        exitProgram()
        
    traverseAgain()

def exitProgram():
    print("\nThank you for using Humber ATM Service.\nHave a nice day")

def takePin():
    global trial
    global userPin
    if(trial <= 3):
        userPin = int(input("Please enter your 4 digit pin: "))
        if(validate(userPin)):
            print("You entered your pin correctly")
            openAccount()
        else:
            print("Incorrect pin")
            trial = trial + 1
            takePin()
    else:
        print("\nFor security reasons you cannot login")
        exitProgram()

def traverseAgain():
    back = input("\nWould you like to go back? >> ")
    if(back == 'yes' or back == 'y'):
        openAccount()
    elif(back == 'no' or back == 'n'):
        exitProgram()
    else:
        print("Invalid input")
        traverseAgain()
        
print("\n-------------------------------------------------------------")
print("Welcome to Humber ATM Service")
takePin()
print("-------------------------------------------------------------\n")
        
    
    

    
    
    
