import math
import random

GOD_MODE = True
GOD_MODE_LIMIT_OF_NUMBERS = 3

def create_random_list(start, end, count):
    result = []
    for i in range(count):
        result.append(random.randint(start,end))

    return result

def play_game(list):
    for i in range(GOD_MODE_LIMIT_OF_NUMBERS): 
        if GOD_MODE:
            print("god mode", list[i])
        user_guess = int(input("Enter an integer from 1 to 99: "))
        while list[i] != user_guess:
            if user_guess < list[i]:
                print("guess is low")
                user_guess = int(input("Enter an integer from 1 to 99: "))
            elif user_guess > list[i]:
                print("guess is high")
                user_guess = int(input("Enter an integer from 1 to 99: "))
            else:
                break
        print("you guessed it!")



first_list_of_int_to_guess = create_random_list(1, 99, 10)
play_game(first_list_of_int_to_guess)

second_list_of_int_to_guess = create_random_list(1, 49, 10)

play_game(second_list_of_int_to_guess)
