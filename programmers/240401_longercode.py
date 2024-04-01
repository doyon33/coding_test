#https://school.programmers.co.kr/learn/courses/30/lessons/120831

import math

def solution(n):
    if n < 1:
        return ("input value is over the range")
    elif n > 1000:
        return ("input value is over the range")
    else:
        if (str(type(n)) == "<class 'int'>"):
            i = 1
            total = 0
            while (i <= n):
                total += returnEvenNumb(i)
                i += 1
            return total
        else:
            return ("input value is not integer")
                

def returnEvenNumb(n):
    q = 0
    r = 0
    q = math.floor(n / 2)
    r = n - q * 2
    
    if (r == 0):
        return n
    else:
        return 0
    
