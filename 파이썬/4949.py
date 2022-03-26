"""
각 줄마다 해당 문자열의 괄호들이 균형을 이루고 있으면 "yes"를, 아니면 "no"를 출력한다.
"""

while True:
    a = input()  # 한줄을 a에 저장한다
    lis = []  # 활용할 빈 리스트

    if a == ".":
        break  # 마지막 줄(.) 이 될 때까지 while 반복문을 실행한다.

    for i in a:
        if i in ["(", "["]:  # 여는 괄호는 무조건 추가한다
            lis.append(i)
        elif i == ")":  # 닫는 괄호는 조건이 필요하다
            if len(lis) != 0 and lis[-1] == "(":  # lis에 마지막으로 추가한 요소가 같은 여는 괄호일 때
                lis.pop()  # (와 )이 만났으므로 lis에서 지운다
            else:
                lis.append(i)  # gjwo(djfoid)gjowkdjg) <- 이것처럼 마지막괄호가 틀렸을 경우엔 lis가 빈 상태로 break 되는데 lis가 빈 상태일때 yes로 하기 때문에 no로 만들기 위해 추가한다.
                break
        elif i == "]":
            if len(lis) != 0 and lis[-1] == "[":
                lis.pop()
            else:
                lis.append(i)
                break

    if len(lis) > 0:  # ([(())]) 0 ([(()] 4 ()[()]] 1
        print("no")
    else:
        print("yes")
