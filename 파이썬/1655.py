# 가운데 값 말하기
import sys
import heapq


n = int(sys.stdin.readline())
max_h, min_h = [], []  # 중간을 기준으로 왼쪽과 오른쪽 힙

for _ in range(n):
    num = int(sys.stdin.readline())
    # 일단 왼쪽 -> 오른쪽 순서로 값을 넣어준 후
    if len(max_h) == len(min_h):  # 홀수번째
        heapq.heappush(max_h, (-num, num))  # 내림차순으로 정렬된다
    else:  # 짝수번째
        heapq.heappush(min_h, (num, num))  # 오름차순으로 정렬된다

    # 왼쪽의 최대값과 오른쪽의 최소값을 비교
    # 최종적으로 왼쪽의 마지막값(최대값)보다 오른쪽의 첫번째값(최소값)이 커야하므로
    # 왼쪽값이 클때는 둘이 서로 바꿔준다
    if len(max_h) >= 1 and len(min_h) >= 1 and max_h[0][1] > min_h[0][1]:
        max_value = heapq.heappop(max_h)[1]
        min_value = heapq.heappop(min_h)[1]
        heapq.heappush(max_h, (-min_value, min_value))
        heapq.heappush(min_h, (max_value, max_value))

    # 최종 힙이 홀수개면 그대로 중간값 [OOX][OO], 짝수개면 중간값 두개의 홀수번째값이 [OOX][XOO] 왼쪽힙의 가장 큰 값이된다.
    print(max_h[0][1])

"""
max_h 내림차순 min_h 오름차순
반으로 나눴을때 왼쪽의 max값이 답이된다.
[1,5,2,10,-99,7,5]
n=0, max_h=[1,] min_h=[]
n=1, max_h=[1,] min_h=[5,]
n=2, max_h=[2,1,] min_h=[5,] => [1,2,5]
n=3, max_h=[2,1,] min_h=[5,10] => [1,2,5,10]
n=4, max_h=[2,1,-99] min_h=[5,10]
n=5, max_h=[2,1,-99] min_h=[5,7,10]
n=6, max_h=[5,2,1,-99] min_h=[5,7,10]
"""
