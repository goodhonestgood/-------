import sys
from collections import deque

t = int(input())

for i in range(t):
    p = sys.stdin.readline().rstrip()  # 수행할 함수
    n = int(input())  # 배열의 길이
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")  # 배열 숫자부분에서 ,으로 나누어 저장
    queue = deque(arr)  # 큐로 만든다.

    rev = 0
    front, back = 0, len(queue) - 1
    flag = 0
    if n == 0:  # 수행할 배열이 없을 때
        queue = []
        front = 0
        back = 0

    for j in p:  # 수행할 함수를 하나씩
        if j == 'R':  # 뒤집기
            rev += 1  # 몇번뒤집는지 추가
        elif j == 'D':  # 버리기
            if len(queue) < 1:  # 배열의 크기가 0이면 break
                flag = 1
                print("error")  # error 출력
                break
            else:
                if rev % 2 == 0:  # 짝수번뒤집혀서 원상태일때
                    queue.popleft()  # 앞에서 버리는 메소드
                else:  # 홀수번뒤집혀서 반대일때
                    queue.pop()  # 뒤가 앞이 돼서 뒤에서 버리기

    if flag == 0:  # 배열의 크기가 1이상일때
        if rev % 2 == 0:  # 뒤집힌 결과에 따라 출력
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")