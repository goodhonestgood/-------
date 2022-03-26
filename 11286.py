# 절대값 힙
# 절대값이 가장 작은 값을 출력하고 그 값을 배열에서 제거한다
import sys
import heapq


N = int(input())
max_h, min_h = [], []
hpop = None

for _ in range(N):
    x = int(sys.stdin.readline())
    if x < 0:  # x가 음수이면 내림차순으로 정렬하는 왼쪽힙에 넣고
        heapq.heappush(max_h,(-x,x))  # 절대값으로 저장
    elif x > 0:  # 양수이면 오름차순 정렬인 오른쪽힙에 넣는다
        heapq.heappush(min_h, (x, x))
    elif x == 0:  # x가 0일땐 제거하면서 출력해야한다
        # 두 힙이 모두 비어있을 때
        if len(max_h) == 0 and len(min_h) == 0:
            print(0)

        # 왼쪽힙의 최대값이 오른쪽힙의 최소값보다 작거나 같을 때 왼쪽힙의 최대값을 출력한다.
        # 또는 왼쪽힙만 존재할때 왼쪽힙의 최대값을 출력한다.
        elif (len(max_h) > 0 and len(min_h) > 0 and max_h[0][0] <= min_h[0][0]) or (len(max_h) > 0 and len(min_h) == 0):
            hpop = heapq.heappop(max_h)
            print(hpop[1])

        # 왼쪽힙의 최대값이 오른쪽힙의 최소값보다 클 때 오른쪽힙의 최소값을 출력한다.
        # 또는 오른쪽힙만 존재할때 오른쪽힙의 최소값을 출력한다.
        elif (len(max_h) > 0 and len(min_h) > 0 and max_h[0][0] > min_h[0][0]) or (len(max_h) == 0 and len(min_h) > 0):
            hpop = heapq.heappop(min_h)
            print(hpop[1])


"""
n=0, max_h=[], min_h=[1,]
n=1, max_h=[-1,], min_h=[1,]
n=2, max_h=[], min_h=[1,] -1
n=3, max_h=[], min_h=[] 1
n=4, max_h=[], min_h=[18,] 1
"""



