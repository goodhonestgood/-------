# 피보나치 수
"""O(N)
def fibo(n):
    if n == 2:
        return 1
    a = fibo(n-1)
    b = fibo(n-2)
    return a+b

n = int(input())
print(fibo(n))
"""
# O(logN)
import sys

input = sys.stdin.readline

# 행렬 A의 B제곱
B = int(input())
A = [[1, 1], [1, 0]]  # 초기값


# 2제곱하는 함수
def power(a, b):
    cal = []
    for i in range(2):
        temp = []
        for j in range(2):
            num = 0
            for k in range(2):
                num += a[i][k] * b[k][j]
            temp.append(num % 1000000007)
        cal.append(temp)
    return cal

# a^8 = a^4 * a^4
# a^4 = a^2 * a^2
# a^2 = a * a

# s = A b = B
def dac(s, b):
    if b == 1:
        return s  # b가 1이면 그대로 s(=A) 가 된다

    a = dac(s, b // 2)  # b가 반씩 줄어들면서 다시 호출된다

    cal = power(a, a) # a 제곱하기

    result = []
    if b % 2: # b가 홀수 일때는 a^5 = a^2 * a^2 * a
        result = power(cal, A) # a 한번더 곱해주기
    else:
        result = cal

    return result

print(dac(A, B)[0][1])