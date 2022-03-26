import sys
from itertools import combinations

n = int(input()) # n/2
mans = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

candidate = [i for i in range(n)]
result = sys.maxsize  # 처음에 최소값을 구할때 가장 큰 int값과 비교하기 위해서.
for comb in combinations(candidate, n // 2): # n//2명으로 된 사람의 조합
    start = list(comb)
    link = candidate - start

    score = 0
    for i in range(1, n // 2):
        for j in range(i):
            score += mans[start[i]][start[j]] + mans[start[j]][start[i]]
            score -= mans[link[i]][link[j]] + mans[link[j]][link[i]]
    result = min(abs(score), result)

print(result)