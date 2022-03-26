#N번째 종말수
def final_number(n):
    a = 0 # n번째와 a번째를 비교할 변수
    i = 666 # 1번째는 무조건 666부터
    
    while N != a:
        if '666' in str(i):
            a += 1
            if N == a:
                return i # 결과 리턴을 하며 함수를 나간다.
        i += 1 # i 숫자가 커지면서 루프를 돈다.

N = int(input())
print(final_number(N))
