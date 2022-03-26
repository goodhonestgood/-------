# 나보다 큰 사람의 수를 세는 것이 목표
N = int(input()) # 총 숫자 입력
people = [(tuple(map(int,input().split())),i) for i in range(N)] # 각 정보 입력하면서 인덱스도 같이 저장 [((55, 185), 0), ((58, 183), 1), ((88, 186), 2), ((60, 175), 3), ((46, 155), 4)]
people_sort = sorted(people, key=lambda x : (-x[0][0], -x[0][1])) # people을 몸무게순 키순으로 일단 정렬 [((88, 186), 2), ((60, 175), 3), ((58, 183), 1), ((55, 185), 0), ((46, 155), 4)]

# 위 정렬된 리스트에서 만약 3번째 사람을 비교할땐 1,2번째 사람과 값을 비교
for idx,per1 in enumerate(people_sort):
    a = 0
    for big_list_per in people_sort[:idx]:
        if big_list_per[0][0] > per1[0][0] and big_list_per[0][1] > per1[0][1]: # 몸무게와 키 모두 큰 사람만
            a += 1 # 큰 사람의 수 
    people_sort[idx] += (a+1,) # 만약 1,2번째 사람과 모두 비교가 끝났을 때 큰 사람의 수(a)만큼 people_sort에 값을 추가한다.

result_list = sorted(people_sort, key=lambda x: x[1]) # 큰 사람의 수가 추가된 리스트를 다시 처음의 인덱스 기준으로 정렬한다. [((55, 185), 0, 2), ((58, 183), 1, 2), ((88, 186), 2, 1), ((60, 175), 3, 2), ((46, 155), 4, 5)]
print(' '.join([str(grade[2]) for grade in result_list])) # 결과

