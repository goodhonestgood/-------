# 분해합
# n 생성자 m 원래숫자
n = int(input())
m = 2

while True:
    msum = 0
    msum += m
    msum += sum(list(map(int,str(m))))

    if msum == n:
        print(m)
        break
    if m > n:
        print(0)
        break
    m+=1
