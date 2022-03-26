import sys
# 가장 큰 직사각형
def func(recs):
    t = len(recs)*1
    t = max(t, recs[0])
    counts = 1
    for i in range(1,len(recs)):
        if recs[i-1] <= recs[i]:
            counts+=1
        else:
            counts = 0
        t = max([c * recs[i + 1 - c] for c in range(1,counts+1)]+[recs[i],t])
    return t

input = sys.stdin.readline
while True:
    case = list(map(int,input().split()))
    if case[0] == 0:
        break

    print(func(case))