N, K = map(int,input().split())

n_list = [i for i in range(1,N+1)]
delist = []
c = K
i = 0
for _ in range(N):
    a = 0
    while a < K:
        if n_list[i] > 0:
            a+=1
        if a == K:
            delist.append(n_list[i])
            n_list[i] = 0
            break
        else:
            i = (i + 1) % N

print("<",end="")
print(*delist,sep=" ,",end="")
print(">")

"""
from collections import deque

queue = deque()
answer = []

n, k = map(int, input().split())

for i in range(1, n+1):
    queue.append(i)

while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())

print("<",end='')
for i in range(len(answer)-1):
    print("%d, "%answer[i], end='')
print(answer[-1], end='')
print(">")
"""