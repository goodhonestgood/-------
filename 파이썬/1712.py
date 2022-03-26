'''
A,B,C=map(int,input().split())
n = 1
if C - B > 0:
    while(n):
        sumAB = A + B*n
        sumC = C*n
        
        if sumAB < sumC:
            print(n, sumAB, sumC)
            break;
        else:
            n += 1
else:
    n = -1
print(n)

'''
A,B,C=map(int,input().split())
n = A + C - B
if C - B > 0:
    while(n):
        sumAB = A + B*n
        sumC = C*n
        
        if sumAB >= sumC:
            n += 1
            break;
        else:
            n -= 1
else:
    n = -1
print(n)


