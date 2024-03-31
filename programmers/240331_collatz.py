def solution(num):
    temp = num
    result = 0
    
    if (num > 1 and num <= 8000000):
        while (temp != 1 and result != 500):
            if (temp % 2 == 0):
                temp /= 2
                result += 1
            else:
                temp = temp * 3 + 1
                result += 1
        if (temp == 1):
            return result
        elif (result == 500):
            return -1
    else:
        return 0
    
# print(solution(6))
