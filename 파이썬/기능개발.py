from collections import deque
def solution(progresses, speeds):
    dq = deque(progresses)
    speeds = deque(speeds)
    ans = []
    while dq:
        for i in range(len(speeds)):
            if dq[i] < 100:
                dq[i] += speeds[i]
        counts = 0
        while dq and dq[0] >= 100:
            dq.popleft()
            speeds.popleft()
            counts += 1
        if counts > 0:
            ans.append(counts)
    return ans