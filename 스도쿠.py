import sys

strs = '0 3 5 4 6 9 2 7 8 7 8 2 1 0 5 6 0 9 0 6 0 2 7 8 1 3 5 3 2 1 0 4 6 8 9 7 8 0 4 9 1 3 5 0 6 5 9 6 8 2 0 4 1 3 9 1 7 6 5 2 0 8 0 6 0 3 7 0 1 9 5 2 2 5 8 3 9 4 7 6 0'
str_list = list(map(int,strs.split()))

board = [str_list[:9],str_list[9:18],str_list[18:27],str_list[27:36],str_list[36:45],str_list[45:54],str_list[54:63],str_list[63:72],str_list[72:81]]
'''
board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
'''
zeros = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0] # [(0,0),(1,3)...]


def get_possibles(r, c):
    possibles = set(range(1, 10)) # 1~9 라는 집합에서
    possibles -= set(board[r]) # r번째 row의 각 col에 해당하는 숫자를 뺀다.
    
    test = set() # 세로 값을 저장할 빈 집합
    for i in range(9):
        test.add(board[i][c]) # c열(세로)의 모든 값을 test에 저장
        
    possibles -= test # test에 저장된 세로줄의 숫자들을 뺀다.

    '''
    test = set() # 
    for i in range(r//3*3, r//3*3+3):
        for j in range(c//3*3, c//3*3+3):
            test.add(board[i][j])
    possibles -= test
    return tuple(possibles)
    '''
    return possibles

def solve(i):
    if i == len(zeros): # zeros 안에 모든 0 값의 좌표가 담겨있다.
        [print(*row) for row in board]
        sys.exit() # 함수를 종료하는 코드
    r, c = zeros[i] # i 번째 0 값의 좌표
    possibles = get_possibles(r, c) # 맞는 값을 찾아 저장

    for num in possibles: # 유망한 값들으
        board[r][c] = num # i번째 좌표에 해당하는 값을 저장
        solve(i+1) # 그 다음 zeros 좌표로 이동
        # board[r][c] = 0

solve(0)
