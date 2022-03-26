import sys

"""
재현이는 잘못된 수를 부를 때마다 0을 외쳐서, 가장 최근에 재민이가 쓴 수를 지우게 시킨다.
재민이는 이렇게 모든 수를 받아 적은 후 그 수의 합을 알고 싶어 한다.
"""

result = []  # 활용할 빈 리스트
for _ in range(int(sys.stdin.readline())):  # n줄
    r = int(sys.stdin.readline())  # 값
    if r == 0:
        result.pop()  # 리스트의 마지막을 지우기
    else:
        result.append(r)  # 리스트에 추가하기

print(sum(result))  # 리스트 합계


"""
class stack:
    def __init__(self):
        self.stacklist = []

    def pushX(self, x):
        self.stacklist.append(x)

    def size(self):
        return len(self.stacklist)

    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0

    def pop(self):
        if self.empty():
            pass
        else:
            self.stacklist.pop()


s = stack()

for _ in range(int(sys.stdin.readline())):
    r = int(sys.stdin.readline())
    if r == 0:
        s.pop()
    else:
        s.pushX(r)
print(s)
"""