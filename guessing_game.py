import math
import random
a = [] #initialization of an empty list
a.append(random.randint(1, 99)) #appending a random number to the list from a range between 1 and 99
a.append(random.randint(1, 99)) #appending a random number to the list from a range between 1 and 99
a.append(random.randint(1, 99)) #appending a random number to the list from a range between 1 and 99
a.append(random.randint(1, 99)) #appending a random number to the list from a range between 1 and 99
a.append(random.randint(1, 99)) #appending a random number to the list from a range between 1 and 99
a.append(random.randint(1, 99)) #appending a random number to the list from a range between 1 and 99
a.append(random.randint(1, 99)) #appending a random number to the list from a range between 1 and 99
a.append(random.randint(1, 99)) #appending a random number to the list from a range between 1 and 99
a.append(random.randint(1, 99)) #appending a random number to the list from a range between 1 and 99
a.append(random.randint(1, 99)) #appending a random number to the list from a range between 1 and 99
#a size = 10
#a[0] - pierwszy
#a[1] - drugi
for i in range(10): # guess 10 numbers from the list 'a' 
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
for i in range(10):
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
