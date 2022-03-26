# n!
n = int(input())
fac = 1
counts = 0
for i in range(n,1,-1):
    fac *= i
    while fac % 10 == 0:
        counts+=1
        fac = fac//10
print(counts)

