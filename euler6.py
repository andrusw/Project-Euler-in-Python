#The sum of the squares of the first ten natural numbers is,
#1^2 + 2^2 + ... + 10^2 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)^2 = 55^2 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum
# is 3025 − 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

limit = 100
nums = range(1,limit+1)
#print([x for x in nums])
squared = [x**2 for x in nums]
#print(squared)

sumSquared = sum(squared)
squaredSum = sum(nums)**2

print(squaredSum - sumSquared)

