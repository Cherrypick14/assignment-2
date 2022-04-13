# a program to check if a number is a perfect square
#    import the math library

import math

#   ask user for an input
number = int(input("enter a number: "))

 #  get the square root
root = math.sqrt(number)

if  int(root + .5) ** 2 == number:
   print(number, "is a perfect square")
else:
   print(number, "ain't a perfect square")    
 



