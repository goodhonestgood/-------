'''
from functools import reduce

n = int(input())
result = reduce(lambda x,y: x*y, range(1,n+1))
print(result)
'''
n = int(input())
result = 1
for i in range(1,n+1):
    result *= i
print(result)


'''
def factorial(s):
    global n
    n -= 1
    if n == 1:
        return s
    else:
        return factorial(s*n)


n = int(input())
print(factorial(n))'''