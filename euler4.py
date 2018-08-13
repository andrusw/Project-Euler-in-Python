#A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

largest = 0
bestX = 0
bestY = 0

def isPalidrome(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False


for x in range(999,99,-1):
    for y in range(999,99,-1):
        if x*y > largest and isPalidrome(x*y):
            largest = x*y
            bestX = x
            bestY = y

print(str(bestX),' * ',bestY,' = ',largest,)
