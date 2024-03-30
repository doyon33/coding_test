# https://school.programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):
    
    i, j = 0, 0
    lost.sort()
    reserve.sort()
    
    double = list(set(lost).intersection(reserve))
    total = n - len(lost) + len(double)

    for j in range(len(double)):
        reserve.remove(double[j])
        lost.remove(double[j])

    for i in range(len(lost)):
        checknum = lost[i]
        if (checknum - 1) in reserve:
            reserve.remove(checknum - 1)
            total += 1
        elif (checknum + 1) in reserve:
            reserve.remove(checknum + 1)
            total += 1
        else:
            continue
    answer = total
    return answer
