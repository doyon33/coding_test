#https://school.programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    first_range = 0
    second_range = 1
    i, j = 0, 0
    result = set()
    
    for i in range(first_range, len(numbers)):
        for j in range(second_range, len(numbers)):
            temp = numbers[i] + numbers[j]
            result.add(temp)
        first_range += 1
        second_range += 1
    
    answer = list(result)
    answer.sort()
    return answer
