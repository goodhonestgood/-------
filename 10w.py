
def solution(line):
    min_x, max_x = float('inf'), -float('inf')
    min_y, max_y = float('inf'), -float('inf')
    result = []
    n = len(line)
    for n1 in range(n-1):
        A1,B1,C1 = line[n1]
        for n2 in range(n1+1,n):
            A2,B2,C2 = line[n2]
            
            if B1 == 0: B1 = 1
            if B2 == 0: B2 = 1
                
            if A1 - A2 != 0:
                a = ((C2/(-B2))+(C1/(B1)))/(-A1/B1 + A2/B2)
                b = A1/(-B1)*a + C1/(-B1)

                if a%1 == 0 and b%1 == 0:
                    result.append([int(a),int(b)])             
    result2 = []
    if result:
        min_x = min([x for x,y in result])
        max_x = max([x for x,y in result])
        min_y = min([y for x,y in result])
        max_y = max([y for x,y in result])
        print(min_x,max_x,min_y,max_y)
        print(result)
        
        
        for i in range(max_y,min_y-1,-1):
            result1 = ''
            for j in range(min_x,max_x+1,1):
                if [j,i] in result:
                    result1 += '*'
                else:
                    result1 += '.'
            result2.append(result1)
    return result2
'''
def solution(line):
    answer = []
    loc = []
    min_x, max_x = float('inf'), -float('inf')
    min_y, max_y = float('inf'), -float('inf')
    length = len(line)
    for i in range(length):
        a1, b1, c1 = line[i]
        for j in range(length):
            if i == j: 
                continue
            a2, b2, c2 = line[j]
            x, y = (b1*c2-b2*c1)/(a1*b2-a2*b1), -((b1*c2-b2*c1)/(a1*b2-a2*b1))*(a1/b1)-(c1/b1)
            if x == int(x) and y == int(y):
                loc.append([int(x), int(y)])
                min_x, max_x = min(min_x, int(x)), max(max_x, int(x))
                min_y, max_y = min(min_y, int(y)), max(max_y, int(y))

    answer = [["." for _ in range(max_x-min_x+1)] for _ in range(max_y-min_y+1)]
    loc = list(map(lambda x: [x[0]-min_x, abs(x[1]-max_y)], loc))
    for x, y in loc:
        answer[y][x] = "*"
    answer = list(map(lambda x: ''.join(x), answer))
    for a in answer:
        print(a)
    return answer
'''
a = solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]])
print(a)
