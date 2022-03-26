N = 6
numbers = [50, 10, 20, 10, 30, 20]
"""
import sys

N = int(input())
numbers = list(map(int, sys.stdin.readline().split()))"""
LIS = [1] * N
for i in range(1, N):
    for j in range(i):
        if numbers[i] > numbers[j]:
            LIS[i] = max(LIS[i], LIS[j]+1)

print(max(LIS))

"""
LIS = [1,1,1,1,1,1]  # 총 개수에서 자기 자신을 포함하기 때문에 
i = 1 LIS = [1,2,1,1,1,1]
i = 2 LIS = [2,3,2,3,1,1]
i = 3 LIS = [1,2,1,3,1,1]
i = 4 LIS = [1,2,1,3,2,1]
i = 5 LIS = [1,2,1,3,2,4]
"""
