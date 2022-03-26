'''
def fibo(a,b,n): #a는 1번째부터 b는 0번째부터 시작 n번루프를 돌면 (n+1번째, n번째수)
    n -=1
    if n == 0:
        return a #결과는 밑 fibo(a+b,a,n)에서 보여지듯 n번째 수가 되는 a
    return fibo(a+b,a,n) 

'''
def fibo(a,b,n): #a는 1번째부터 b는 0번째부터 시작 n번루프를 돌면 (n+1번째, n번째수)
    for _ in range(n):
        c = a # a+b에서 값이 변하는 걸 방지
        a = a+b
        b = c 
    return b # 결과는 n번째 자리인 b

n = int(input())
result = fibo(1,0,n)
print(result)
