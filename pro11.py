import pprint
'''
a= [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 1, -9, -9, -9, -10, -10, -10, 1, 0], [0, 1, -9, -20, -9, -10, -9, -9, 1, 0], [0, 1, 2, -9, 2, 1, 2, 2, 1, 0], [0, 0, 1, -10, 1, 0, 1, 1, 0, 0], [0, 0, 1, -9, 2, 1, 2, 2, 1, 1], [0, 0, 1, -9, -9, -10, -9, -9, -10, 1], [0, 0, 1, -9, 2, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 0, 0, 0, 0, 0]]
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] < 0:
            a[i][j] = 0
pprint.pprint(a)

b = [[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]]
c = sorted(b,key=lambda x : abs(x[0]-x[2])*abs(x[1]-x[3]))
print(c)
'''


def solution(rectangle, characterX, characterY, itemX, itemY):
    max_x = [i[0] for i in rectangle] + [i[2] for i in rectangle]
    max_x = max(max_x)
    max_y = [i[1] for i in rectangle] + [i[3] for i in rectangle]
    max_y = max(max_y)

    rectangle = sorted(rectangle, key=lambda x: abs(x[0] - x[2]) * abs(x[1] - x[3]))
    rectangle_list = [[0 for _ in range(max_x + 2)] for _ in range(max_y + 2)]

    for r in rectangle:
        for i in range(r[1], r[3] + 1):
            if i in [r[1], r[3]]:
                for j in range(r[0], r[2] + 1):
                    rectangle_list[i][j] += 1
            else:
                rectangle_list[i][r[0]] += 1
                rectangle_list[i][r[2]] += 1
                for k in range(r[0] + 1, r[2]):
                    rectangle_list[i][k] -= 10

    if characterY > itemY:
        x, y = characterX, characterY
        characterX, characterY = itemX, itemY
        itemX, itemY = x, y

    pprint.pprint(rectangle_list)
    '''
    # 왼 아 오 위
    n1 = 1
    while True:
        rectangle_list[characterY][characterX] = 0
        if rectangle_list[characterY][characterX - 1] >= 1:
            characterX = characterX - 1
        elif rectangle_list[characterY + 1][characterX] >= 1:
            characterY = characterY + 1
        elif rectangle_list[characterY][characterX + 1] >= 1:
            characterX = characterX + 1
        elif rectangle_list[characterY - 1][characterX] >= 1:
            characterY = characterY - 1

        if characterX == itemX and characterY == itemY:
            break
        else:
            n1 += 1
    

    # 오 위 왼 아
    n2 = 1
    while True:
        rectangle_list[characterY][characterX] = 0
        if rectangle_list[characterY][characterX + 1] >= 1:
            characterX = characterX + 1
        elif rectangle_list[characterY - 1][characterX] >= 1:
            characterY = characterY - 1
        elif rectangle_list[characterY][characterX - 1] >= 1:
            characterX = characterX - 1
        elif rectangle_list[characterY + 1][characterX] >= 1:
            characterY = characterY + 1

        if characterX == itemX and characterY == itemY:
            break
        else:
            n2 += 1

    return n1 if n1 <= n2 else n2
'''
result = solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],1,3,7,8)
print(result)