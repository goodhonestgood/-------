n = int(input())
a = list(map(int, input().split()))
sum = [a[0]]  # 합의 최대값 저장

for i in range(len(a) - 1):
    sum.append(max(sum[i] + a[i + 1], a[i + 1]))
print(max(sum))


