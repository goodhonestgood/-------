K, N = 4, 11
lan = [802,743,457,539]
"""
import sys

K, N = map(int, input().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]"""

start, end = 1, max(lan)  # 이분탐색 처음과 끝위치

while start <= end:  # start가 계속 높아지다가 마지막으로 end가 낮아지면 end가 계속 낮아지다가 start가 높아지면 끝
    mid = (start + end) // 2  # 중간 위치

    lines = 0  # 랜선 수
    for i in lan:
        lines += i // mid  # 중간값으로 분할 된 랜선 수

    if lines >= N:  # 예를들어 802//2=401로 모든 랜선을 나눴을 때 11개 이상이다
        start = mid + 1  # start를 높여서 중간값mid를 올린다
    else:
        end = mid - 1  # end를 낮춰서 중간값을 내린다

print(end)

