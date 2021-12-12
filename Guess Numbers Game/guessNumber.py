#Author : Akshar
#ID     : N01418888
#Date   : Nov 27, 2021

import random

gen_num = 0
guess = 0

def create_line():
    print("\n-------------------------------------------------------")

def design():
    print("*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")
    
def num_generator():
    global gen_num
    gen_num = random.randint(1, 10)
    
def take_input():
    global guess
    global gen_num
    create_line()
    guess = input("Please guess the random number: ")
    if(guess.lower() == 'n'):
        print("\n<<<<<<<<<<<<Game Stopped>>>>>>>>>>>>\n")
    else:
        guess = int(guess)
        validate(guess, gen_num)

def validate(guess, gen_num):
    while(True):
        if(guess == gen_num):
            create_line()
            design()
            print("*.*.*.* Viola! You guessed the right number *.*.*.*")
            design()
            break
        elif(guess > gen_num):
            print("Hint(Pick a smaller number): ")
            take_input()
            break
        elif(guess < gen_num):
            print("Hint(Pick a larger number): ")
            take_input()
            break
        else:
            print("Error")
            break

create_line()
print("At any point if you wish to not play the game, press: n")
num_generator()
take_input()



        

    
    
        


