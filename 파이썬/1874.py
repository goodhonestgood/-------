n = int(input())
s = []
op = []
count = 1

for i in range(n):
    num = int(input())
    while count <= num:
        s.append(count)
        op.append('+')
        count += 1
    if s[-1] == num:
        s.pop()
        op.append('-')

# 출력
if not op:
    print('NO')
else:
    for i in op:
        print(i)
