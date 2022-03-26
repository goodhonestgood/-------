M,N = map(int,input().split())
'''
남은 리스트가 모두 소수일때 멈추는 코드
효율적이지 않다

remove_list = list(range(2,N+1))
result_list = []
list_len = 0
if M == 2 or N == 2:
    result_list.append(2)

for i in remove_list:
    remove_list = list(map(int,filter(lambda x: x%i != 0, remove_list)))
    if remove_list:
        if list_len == len(remove_list): 
            pass
        elif list_len -1 == len(remove_list):
            result_list += [i for i in remove_list if M <= i <= N]
            break
        else:
            if M <= remove_list[0] <= N:
                result_list.append(remove_list[0])
                list_len = len(remove_list)

result = sorted(list(set(result_list)))
for i in result:
    print(i)  
'''

def is_prime_num(n):
    for i in range(2, int(n**0.5)+1): # 이 이상의 값은 지우나 마나
        if n % i == 0: # 소수가 아니다.
            return False

    return True # 소수이다.

for i in range(M,N+1):
    if i > 1: # 1은 어처피 소수가 아니다.
        if is_prime_num(i):
            print(i)
        elif i == 2: # 2의 경우만 예외로 처리한다.
            print(i)
