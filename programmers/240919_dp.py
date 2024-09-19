def solution1(money):
    answer = 0
    lenOfList = len(money)
    temp = [0] * (lenOfList - 1)
    temp[0] = money[0]
    temp[1] = money[1]
    temp[2] = temp[0] + money[2]
    for i in range(3, lenOfList-1):
        temp[i] = money[i] + max(temp[i-2], temp[i-3])
    max1 = max(temp)

    temp[0] = money[1]
    temp[1] = money[2]
    temp[2] = temp[0] + money[3]
    for i in range(4, lenOfList):
        # print(i)
        temp[i-1] = money[i] + max(temp[i-3], temp[i-4])
    max2 = max(temp)
    answer = max(max1, max2)
    return answer

def solution2(s):
    answer = ''
    arr = s.split(" ")
    for _ in range(len(arr)):
        arr[_] = int(arr[_])
    maxArr = max(arr)
    minArr = min(arr)
    answer = str(minArr)+" "+str(maxArr)
    return answer
