import sys


class stack():
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
            print(-1)
        else:
            print(self.stacklist.pop())

    def top(self):
        if self.empty():
            print(-1)
        else:
            print(self.stacklist[-1])


s = stack()

for _ in range(int(sys.stdin.readline())):
    r = sys.stdin.readline().split()

    if r[0] == 'push':
        s.pushX(r[1])
    elif r[0] == 'top':
        s.top()
    elif r[0] == 'size':
        print(s.size())
    elif r[0] == 'empty':
        print(s.empty())
    elif r[0] == 'pop':
        s.pop()
