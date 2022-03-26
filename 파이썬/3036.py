"""
N = 4
rings = [300, 1, 1, 300]

원의 둘레 = 2파이r
2*파이*8 / 2*파이*4
(2*파이*4 * 2*파이*8 / 2*파이*4) / 2*파이*2
"""
"""
import sys

N = int(input())
rings = list(map(int, sys.stdin.readline().split()))

a = 1
for i in range(1, N):
    a = rings[i - 1] * a / rings[i]
    if a * 10 % 10 == 0:
        print(str(int(a)) + '/' + str(1))
    elif a * 10 % 5 == 0:
        print(str(int(a*2)) + '/' + str(2))
    elif a * 10 % 2 == 0:
        print(str(int(a*5)) + '/' + str(5))
    else:
        print(str(int(a*10)) + '/' + str(10))

"""
"""
[8,4,2]
원의 둘레 = 2파이r
0번째 = 2*파이*8
1번째 = 2*파이*8 / 2*파이*4
2번째 = (2*파이*4 * 2*파이*8 / 2*파이*4) / 2*파이*2 => 2*파이*8 / 2*파이*2
"""
import sys
from math import gcd

N = int(input())
rings = list(map(int, sys.stdin.readline().split()))
# 답 = 0번째링 / n번째링, 이걸 기약분수로 나타내기 위하여
# 0번째 링과 나머지 각 링의 최대공약수를 구하여 나누어 준다
for i in range(1, N):
    g = gcd(rings[0], rings[i])
    print('{0}/{1}'.format(rings[0] // g, rings[i] // g))
