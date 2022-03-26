def solution(n):
    first = 1  # n=1일때는 무조건 1

    # 맨 앞 숫자만 구한다
    # n=2일때부터 n까지
    for k in range(2, n + 1):
        first += (4 * k - 6)

    # n줄에 숫자가 2n-1개씩 있고 2만큼 늘어난다
    result_list = [first + 2 * (2 * n - 2), first + 2 * (2 * n - 2) - 2, first + 2 * (2 * n - 2) - 4]

    # 합계
    return sum(result_list)


def solution(numArr):
    aver = round(sum(numArr) / 3, 2)  # 평균, 3번째 자리에서 반올림

    level = ''
    if aver >= 90:
        level = 'A'
    elif aver >= 80:
        level = 'B'
    elif aver >= 70:
        level = 'C'
    elif aver >= 60:
        level = 'D'
    else:
        level = 'F'

    aver = "{:.2f}".format(aver)  # ?.00
    return [str(aver), level]


def solution(size):
    """
    긴변의길이 < 나머지길이의합
    a < b+c

    a = size -b -c
    b = (size-c)//2 ~ c b와 c가 반대가 될 때 같아짐
    c = 1~size/3
    """
    count = 0
    for c in range(1, size // 3 + 1):
        for b in range((size - c) // 2, c - 1, -1):
            a = size - b - c
            if a < b + c:
                count += 1
    return count

def solution(num):
    a = num%2
    if a == 0:
        return "짝"
    else:
        return "홀"