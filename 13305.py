n = int(input()) # 도시의 개수
btw = list(map(int,input().split())) # 도시 간 거리 n-1
price = list(map(int,input().split())) # 리터 당 가격 1리터 1키로미터

value = price[0]
result = price[0]*btw[0]
for i in range(1,n-1):
    if value > price[i]:
        value = price[i]
    result += value*btw[i]

print(result)

