from random import randint

print("The program allows you to guess a number between 1-50")

numstack = randint(1,50)
number = int(input("enter a number to start the guess: "))

mycheck ="Oopsy! give it a second try"

while mycheck == "Oopsy! give it a second try":
     feedback = int(input("Please entr a number within the given range: "))
     if feedback > numstack:
        print("The numbr is too high")
     elif feedback < numstack:
        print("The number is very low")
     else:
         print("You have it right")
         mycheck = "Yaay!"
         print(mycheck)

print("see yah in a few")

