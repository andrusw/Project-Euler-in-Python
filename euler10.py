#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

def primesUnder(x):
    primes = [2]
    maybePrimes = range(3,x)
    maybePrimes = list(set(maybePrimes) - (set(range(2,x,2)))) #remove even
    for i in range(3,x,2):
        if i in set(maybePrimes):
            isPrime = True
            for j in primes:
                if i % j == 0:
                    isPrime = False
                    break
            if isPrime:
                primes.append(i)
                maybePrimes = list(set(maybePrimes) - (set(range(i,x,i))))#remove factors of this prime from list
    return primes

#print(sum(primesUnder(10)))
print(sum(primesUnder(2000000)))