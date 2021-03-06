#Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million,
#find the sum of the even-valued terms.


import time
#Recursive attempt --too slow
# def Fibonacci (max):
#     if max == 0 or max == 1:
#         return max
#     else:
#         return Fibonacci(max-2) + Fibonacci(max-1)

# start = time.time()
# seed = 2
# val = 0
# sum = 0

# while val < 4000000:
#     val = Fibonacci(seed)
#     seed+=1

#     if val % 2 == 0:
#         sum += val

# print(sum)
# print(time.time()-start)#478 seconds

def Fibonacci(max):
    if max == 1:
        return [1]
    elif max == 2:
        return [1,2]
    else:
        i = 1
        j = 2
        fibList = [1,2]
        while i+j < max:
            fibList.append(i+j)
            i = fibList[-2]
            j = fibList[-1]
        return fibList
start = time.time()
print(sum(x for x in Fibonacci(4000000) if x % 2 == 0))
print(time.time()-start)#0.0039 sec