n = int(input())
nge = list(map(int,input().split()))

result = []
for i in range(n-1):
    for j in range(i+1,n):
        if nge[j] > nge[i]:
            result.append(nge[j])
            break
        if j == n-1:
            result.append(-1)

result.append(-1)
print(*result)