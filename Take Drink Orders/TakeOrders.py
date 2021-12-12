# AUTHOR : AKSHAR
# DATE: DEC 03, 2021

from datetime import datetime

def begin():
    print("\n----------------------Order Information-----------------------")

def end():
    print("----------------------Thank you " + customerName + "-------------------\n")

def getDate():
    today = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
    return today

def calculateTotal(drink, size, quantity):
    total = 0
    if(drink == "DECAF COFFEE"):
        if(size == "SMALL"):
            total = 1.00
        elif(size == "MEDIUM"):
            total = 1.25
        else:
            total = 1.50
    elif(drink == "LATTE"):
        if(size == "SMALL"):
            total = 1.80
        elif(size == "MEDIUM"):
            total = 2.00
        else:
            total = 2.25
    else:
        if(size == "SMALL"):
            total = 0.80
        elif(size == "MEDIUM"):
            total = 1.10
        else:
            total = 1.30
    return (total * quantity)
            

begin()

customerName = input("Please enter your name: ")

drinkOptions = "\nThere are 03 drink options to choose from"
drinkOptions += "\n1) Decaf coffee \n2) Latte \n3) Black"
print(drinkOptions)

drink = input("Select your drink: ")
quantity = int(input("Quantity: "))

drinkSizes = "\nThere are 03 sizes availalbe"
drinkSizes += "\n1) Small \n2) Medium \n3) Large"
print(drinkSizes)

size = input("Select drink size: ")

total = calculateTotal(drink.upper(), size.upper(), quantity)

today = getDate()
print("\nDate of transaction: " + today)
print("Your order: " + str(quantity) + " " + size.upper() + " " + drink.upper())
print("Order Total: $" + str(total))

#WRITING TO FILE USING APPEND WITH READ AND WRITE MODE (a+)
try:
    file = open("transactions.txt", "a+")
    file.write("Name: " + customerName.upper() + "\nDate: " + today + "\nOrder Items: " + str(quantity) + " " + size.upper() + " " + drink.upper() + "\nTotal: $" + str(total) + "\n\n")
except:
    print("Error occurred")
    raise
finally:
    file.close()

end()

