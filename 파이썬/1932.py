import sys
N = int(input())
tri = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

for i in range(len(tri)-1):
    a = 0
    for j in range(i+1):
        if a == 0: tri[i+1][j] += tri[i][j]
        elif a == 1:
            tri[i+1][j] += (tri[i][j] - tri[i][j-1]) if tri[i][j] > (tri[i][j-1] if j-1 >= 0 else tri[i][j]) else 0
            a = 0
        tri[i+1][j+1] += tri[i][j]
        a = 1
print(max(tri[-1]))
