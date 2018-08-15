#The following iterative sequence is defined for the set of positive integers:
#n → n/2 (n is even)
#n → 3n + 1 (n is odd)
#Using the rule above and starting with 13, we generate the following sequence:
#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#Which starting number, under one million, produces the longest chain?
#NOTE: Once the chain starts the terms are allowed to go above one million.

from time import time

def ifEven(x):
    return int(x/2)

def ifOdd(x):
    return (3*x)+1

def Collatz(seed):
    seqList = [seed]
    while seed != 1:
        if seed % 2 == 0:
            seed = ifEven(seed)
        else:
            seed = ifOdd(seed)
        seqList.append(seed)
    return seqList

start = time()
longestChain = 0
longestSeed = 0

for i in range(1,1000000):
    currentLen = len(Collatz(i))
    if currentLen > longestChain:
        longestSeed = i
        longestChain = currentLen

print('Longest chain length of ' + str(longestChain) + ' with seed ' + str(longestSeed))
print(time() - start)