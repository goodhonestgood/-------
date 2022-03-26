from collections import deque
n,m = map(int,input())
ms = list(map(int,input()))
dq = deque(ms)

front = dq[0]
counts = 0
for i in ms:
    if (front-(i-1)) == 0:
        dq.popleft()
        break
    elif 0 < -(front-(i-1)) <= n//2:
        for _ in range(-(front-(i-1))):
            dq.append(dq.popleft())
            counts +=1
    else:
        for _ in range(-(front-(i-1))):
            dq.appendleft(dq.pop())
            counts +=1
    front = dq[0]
print(counts)

