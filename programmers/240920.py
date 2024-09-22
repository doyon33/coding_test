#https://school.programmers.co.kr/learn/courses/30/lessons/12909
def solution(s):
    answer = False
    count = 0
    for _ in range(len(s)):
        if (s[_] == '('):
            count += 1
        else:
            count -= 1
        
        if (count < 0):
            return answer
    
    if (count == 0):
        answer = True
    return answer

print(solution('()((())'))
# s = '()()))'
# for _ in range(len(s)):
#     print(s[_]+" ")
