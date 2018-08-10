#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#{71: 8462696833, 839: 716151937, 1471: 408464633, 6857: 87625999}
#9085.9359664917 seconds ... too long

from time import time
from math import sqrt

def primeList(x):
    if x < 2:
        return []
    elif x == 2:
        return [2]
    elif x == 3:
        return [2,3]
    else:
        pl = [2]
        maybePrimes = range(3,x)
        maybePrimes = list(set(maybePrimes) - (set(range(2,x,2)))) #remove even
        for i in range(3,x,2):
            if i in set(maybePrimes):
                isPrime = True
                for j in pl:
                    if i % j == 0:
                        isPrime = False
                        break
                if isPrime:
                    pl.append(i)
                    maybePrimes = list(set(maybePrimes) - (set(range(i,x,i))))#remove factors of this prime from list
        return pl

#print(primeList(int(sqrt(13195))+1))

#val = 13195
start = time()
val = 600851475143

primeFactors = {}
for i in primeList(int(sqrt(val))+1):
    if val % i == 0:
        primeFactors[i] = val // i

print(primeFactors)
print(time()-start)
