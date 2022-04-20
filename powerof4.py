#   a program to check if a given positive integer is a power of 4
from math import log, floor

def checkpower_4(num):

   number = log(num) / log(4)

   #    if it's an integer, return true
   return number == floor(number)


if checkpower_4(78):
   print('The number is a power of 4')
else:
   print('The number is not a power of 4')



