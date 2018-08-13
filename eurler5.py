#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#232792560
#Too slow 1495.6332676410675 seconds

from functools import reduce
from math import factorial
from time import time

start = time()
upto = 20
upperLimit = factorial(upto)
smallest = upperLimit

#Too slow for large number
for i in range(2,upperLimit,2): #just even numbers
    found = True
    for j in range(upto,1,-1): #work from top down
        if i % j != 0:
            found = False
            break
    if found:
        smallest = i
        break

print(smallest)
print(time()-start)