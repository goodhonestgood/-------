# 별 찍는 재귀 함수
# draw_star 함수는 가장 작은 모양인 3*3까지 간 후에
# 3*3이 반복되는 부분에 복사되면서 9*9를 만들고
# 다시 9*9가 27*27을 만들고 ...
# 마지막으로 N/3*N/3이 N*N을 만들면 끝난다.
def draw_star(n):
    global Map  # 메인에 있는 변수를 함수안에서도 사용하겠다.

    if n == 3:  # 기본, 3*3 일때 모양
        Map[0][:3] = Map[2][:3] = [1] * 3
        Map[1][:3] = [1, 0, 1]
        return

    a = n // 3
    draw_star(n // 3)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:  # 전체적으로 9등분됐을때 (0,0~3,3) 1,1 부분인 중간은 아무것도 하지 않고 continue
                continue
            for k in range(a):
                Map[a * i + k][a * j:a * (j + 1)] = Map[k][:a]  #  a*a의 모양이 있을 때, k가 0부터 a까지 변하면서 a*a의 모양대로 반복되는 부분에 복사한다. 27*27일때는 9*9가 9번 반복되는 모양


N = int(input())

# 메인 데이터 선언
Map = [[0 for i in range(N)] for i in range(N)]

draw_star(N)

for i in Map:
    for j in i:
        if j:
            print('*', end='')
        else:
            print(' ', end='')
    print()  # 줄바꿈