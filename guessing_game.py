import math
import random

GOD_MODE = True
GOD_MODE_LIMIT_OF_NUMBERS = 3
#1 first functions: function to return a random list of integers from a set range and #
#2 second function: function to guess a number
#3 

a = [] 
a.append(random.randint(1, 99)) 
a.append(random.randint(1, 99)) 
a.append(random.randint(1, 99)) 
a.append(random.randint(1, 99)) 
a.append(random.randint(1, 99)) 
a.append(random.randint(1, 99)) 
a.append(random.randint(1, 99)) 
a.append(random.randint(1, 99)) 
a.append(random.randint(1, 99)) 
a.append(random.randint(1, 99)) 

for i in range(GOD_MODE_LIMIT_OF_NUMBERS): 
    if GOD_MODE:
        print("god mode", a[i])


    g = int(input("Enter an integer from 1 to 99: "))
    while a[i] != g:
        if g < a[i]:
            print("guess is low")
            g = int(input("Enter an integer from 1 to 99: "))
        elif g > a[i]:
            print("guess is high")
            g = int(input("Enter an integer from 1 to 99: "))
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

    g = int(input("Enter an integer from 1 to 49: "))
    while b[i] != g:
        if g < b[i]:
            print("guess is low")
            g = int(input("Enter an integer from 1 to 49: "))
        elif g > b[i]:
            print("guess is high")
            g = int(input("Enter an integer from 1 to 49: "))
        else:
            break
    print("you guessed it!")
