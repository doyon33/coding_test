#https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    num_eng = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    i = 0
    temp = str(s)
    # answer = str(s)
    for i in range(10):
        if num_eng[i] in s:
            index = num_eng.index(num_eng[i])
            temp = temp.replace(num_eng[i], str(index))
        else:
            continue;
            
    answer = int(temp)

    return answer
