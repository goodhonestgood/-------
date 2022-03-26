import sys
# 체스판 만들기
n,m = map(int,input().split())
chess = [sys.stdin.readline() for _ in range(n)]
result = []
for i in range(n-8+1):
    for j in range(m-8+1):
        count1 = 0
        count2 = 0
        for row in range(i,i+8):
            for col in range(j,j+8):
                if (col+row) % 2 == 0:
                    if chess[row][col] == 'W':
                        count2+=1
                    else:
                        count1+=1
                else:
                    if chess[row][col] == 'B':
                        count2+=1
                    else:
                        count1+=1
        result += [count1,count2]
print(min(result))


