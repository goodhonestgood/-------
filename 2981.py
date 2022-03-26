"""
import sys

MS = []
for _ in range(int(input())):
    MS.append(int(sys.stdin.readline()))

result = []
for i in range(2, min(MS)+1):
    a = [x % i for x in MS]
    a_len = len(set(a))
    if a_len == 1:
        result.append(i)

for r in result[:-1]:
    print(r, end=' ')
print(result[-1])
"""

from math import gcd
from math import sqrt

n = int(input())
ns = list(int(input()) for _ in range(n))
ns.sort()  # 입력값을 오름차순으로 정렬

interval = list()
ans = list()
"""
A/M = a .. R

A = M * a + R
B = M * b + R
C = M * c + R

A - B = M ( a - b )
B - C = M ( b - c )

M은 A-B, B-C 공약수가 된다.
"""

# A - B 값들을 interval 리스트에 저장
for i in range(1, n):
    interval.append(ns[i] - ns[i - 1])

# gcd 최대 공약수 구하는 함수
prev = interval[0]
for i in range(1, len(interval)):
    prev = gcd(prev, interval[i])

# 최대공약수의 약수 구하기
for i in range(2, int(sqrt(prev)) + 1):  # 제곱근까지만 탐색
    if prev % i == 0:
        # 18 % 2 = 0
        # 18 // 2 = 9
        # i와 i로 나눴을 때 몫이 18의 약수가 된다.
        ans.append(i)
        ans.append(prev // i)
ans.append(prev)  # 18의 약수는 1,2,3,6,9,18 이므로 자기 자신까지 포함시킨다.

ans = list(set(ans))  # 중복이 있을수 있으니 제거
ans.sort()
print(*ans)