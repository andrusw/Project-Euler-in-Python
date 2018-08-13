#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

#A little slow
#104743
#198.47148823738098

from time import time

def nthPrime(x):
    if x < 0:
        return 1
    elif x == 1:
        return 2
    else:
        primeList = [2]
        current = 3
        while len(primeList) < x:
            isPrime = True
            for p in primeList:
                if current % p == 0:
                    isPrime = False
                    break

            if isPrime:
                primeList.append(current)

            current += 1
        return primeList[x-1]

start = time()
print(nthPrime(10001))
print(time() - start)
