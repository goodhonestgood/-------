import sys

def dist(a,b):
    return (b[0] - a[0]) ** 2 + (b[1] + a[1]) ** 2

def divide_and_conquer(start, end):
    length = end - start
    if length == 2:
        return dist(dots[start], dots[start + 1])
    elif length == 3:
        return min(dist(dots[start], dots[start + 1]), dist(dots[start], dots[start + 2]),
                   dist(dots[start + 1], dots[start + 2]))
    else:  # 분할과 정복
        mid = (start+end)//2
        d = min(divide_and_conquer(start,mid),divide_and_conquer(mid,end))  #  각각 가장 작은 값의 작은 값

        midX = dots[mid][0]
        cmp_list = []
        for i in range(start,end):
            if (dots[i][0]-midX)**2 <= d:  #  왼쪽(오른쪽)의 최소길이인 d보다 짧은 거리에 있는 좌표만
                cmp_list.append(dots[i])

        clist_len = len(cmp_list)
        if clist_len >= 2:
            cmp_list.sort(key= lambda x: x[1])
            for i in range(clist_len - 1):
                for j in range(i + 1, clist_len):
                    if (cmp_list[i][1] - cmp_list[j][1]) ** 2 > d:  # 두 y좌표 차이가 d이상이면 최소길이보다 길다는 뜻
                        break
                    elif cmp_list[i][0] < midX and cmp_list[j][0] < midX:  # 중간좌표보다 두좌표 모두 왼쪽
                        continue
                    elif cmp_list[i][0] >= midX and cmp_list[j][0] >= midX:  # 중간좌표보다 두좌표 모두 오른쪽
                        continue
                    d = min(d, dist(cmp_list[i], cmp_list[j]))  # 최소길이인 d와 위 두 좌표의 길이 중 작은 값을 다시 최소값으로 한다
        return d

n = int(input())
dots = [tuple(map(int,sys.stdin.readline().split())) for _ in range(n)]
dots = list(set(dots))
dots.sort(key = lambda x: x[0])

if n != len(dots):
    print(0)  # 같은 좌표가 있다는 뜻이므로 그 사이의 거리가 0이여서 0을 출력하며 끝낸다.
else:
    print(divide_and_conquer(0, n))

