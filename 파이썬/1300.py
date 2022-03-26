n = int(input())
k = int(input())
start, end = 1,k
ans = 0
while(start <= end):
    mid = (start + end) // 2 # 중간값
    cnt = 0
    for i in range(1, n+1):
        cnt += min(mid//i, n) # i번째 행에서 mid 보다 작은 값

    if cnt >= k: # k번째가 mid보다 앞에 있다는 뜻으로 end를 줄여준다.
        ans = mid
        end = mid-1
    else: # mid 보다 뒤에 K가 존재한다는 뜻으로 start를 줄여준다.
        start = mid+1
print(ans)