import math
import random

GOD_MODE = True
GOD_MODE_LIMIT_OF_NUMBERS = 3
#1 first functions: function to return a random list of integers from a set range and #
#2 second function: function to guess a number
#3 

first_list_of_int_to_guess = [] 
first_list_of_int_to_guess.append(random.randint(1, 99)) 
first_list_of_int_to_guess.append(random.randint(1, 99)) 
first_list_of_int_to_guess.append(random.randint(1, 99)) 
first_list_of_int_to_guess.append(random.randint(1, 99)) 
first_list_of_int_to_guess.append(random.randint(1, 99)) 
first_list_of_int_to_guess.append(random.randint(1, 99)) 
first_list_of_int_to_guess.append(random.randint(1, 99)) 
first_list_of_int_to_guess.append(random.randint(1, 99)) 
first_list_of_int_to_guess.append(random.randint(1, 99)) 
first_list_of_int_to_guess.append(random.randint(1, 99)) 

for i in range(GOD_MODE_LIMIT_OF_NUMBERS): 
    if GOD_MODE:
        print("god mode", first_list_of_int_to_guess[i])


    user_guess = int(input("Enter an integer from 1 to 99: "))
    while first_list_of_int_to_guess[i] != user_guess:
        if user_guess < first_list_of_int_to_guess[i]:
            print("guess is low")
            user_guess = int(input("Enter an integer from 1 to 99: "))
        elif user_guess > first_list_of_int_to_guess[i]:
            print("guess is high")
            user_guess = int(input("Enter an integer from 1 to 99: "))
        else:
            break
    print("you guessed it!")

b = []
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
for i in range(GOD_MODE_LIMIT_OF_NUMBERS):
    if GOD_MODE:
        print("god mode", b[i])

    user_guess = int(input("Enter an integer from 1 to 49: "))
    while b[i] != user_guess:
        if user_guess < b[i]:
            print("guess is low")
            user_guess = int(input("Enter an integer from 1 to 49: "))
        elif user_guess > b[i]:
            print("guess is high")
            user_guess = int(input("Enter an integer from 1 to 49: "))
        else:
            break
    print("you guessed it!")
