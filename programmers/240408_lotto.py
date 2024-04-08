# https://school.programmers.co.kr/learn/courses/30/lessons/77484?language=python3﻿
def solution(lottos, win_nums):
    #iterator
    i = 0
    #min and max value of winning number or ranks
    min, max = 0, 0
    #number of 0 in list lottos
    numOfZero = 0
    #rank dictionary (winning number : rank)
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}

    #count number of winning number(min & max)
    for i in lottos:
        if (i in win_nums): # if lottos[n] is in list win_nums
            min += 1
            max += 1
        elif (i == 0): # if lottos[n] is 0 (unknown value)
            numOfZero += 1
        else:
            continue

    # 0 means that it can be a winning number
    max += numOfZero

    #change min & max values to its ranks
    min = rank[min]
    max = rank[max]

    return [max, min]

#test code
print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
