import sys
# 집, 공유기 개수
N, C = map(int, (input().split()))
house = [int(sys.stdin.readline()) for _ in range(N)] # 집 좌표

# 공유기
def router_counter(distance):
    count = 1
    cur_house = house[0]  # 시작점
    for i in range(1, N):  # 집모두를 돈다
        if cur_house + distance <= house[i]:  # 이전 집에서 해당 거리보다 멀리 떨어진 집이라면
            count += 1
            cur_house = house[i]  # 공유기 설치된 집 갱신
    return count


house = sorted(house)  # 오름차순 정렬
start, end = 1, house[-1] - house[0]  # 1, 첫집과 끝집

while start <= end:  # 이분탐색 알고리즘
    mid = (start + end) // 2

    if router_counter(mid) >= C:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)